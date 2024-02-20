#!/usr/bin/python3.8

"""
Original Author: jmclaus
Altered by: Jaccouille
Description: This script is used to update the map based on recent commits.
It has been modified to generate local versions of the map based on wurst.build.
"""

# Standard library imports:
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from configparser import ConfigParser
from functools import partial
from datetime import date
from getpass import getpass
from itertools import takewhile
from operator import methodcaller
from os import chdir
from os.path import exists, join
from subprocess import run
from sys import exit

# Third-party imports:
from boltons.iterutils import first
from git import Repo
from github import Github
from jinja2 import Template
from parse import search
from yaml import dump, Dumper, load, Loader


# The template for the changelog file.
changelog_template = Template(
    """
package {{ package }}

import ChangeLog

init
    new ChangeLog({{ major }}, {{ minor }}, '{{ patch }}')
{% for change in changelog %}
        ..add("{{change}}")
{% endfor %}
""".lstrip(),
    trim_blocks=True,
)

war3map_skin_template = Template(
"""
[CustomSkin]
InfoPanelIconArmorDivine=UI\Widgets\Console\Human\infocard-armor-spectral.dds

[Errors]
Notancient=Cannot sell building with items/upgrades

[FrameDef]
ARMORTIP_SMALL=Damage received from:|n|cff00FF00Pierce: 200%|r|n|cffFFFFFFMagic: 100%|r|n|cffFFFFFFSiege: 100%|r|n|cffFF0000Normal: 75%|r
ARMORTIP_MEDIUM=Damage received from:|n|cff00FF00Normal: 175%|r|n|cff00FF00Siege: 150%|r|n|cffFF0000Magic: 75%|r|n|cffFF0000Pierce: 75%|r
ARMORTIP_LARGE=Damage received from:|n|cff00FF00Magic: 200%|r|n|cffFFFFFFNormal: 100%|r|n|cffFFFFFFPierce: 100%|r|n|cffFFFFFFSiege: 100%|r
ARMORTIP_FORT=Damage received from:|n|cff00FF00Siege: 200%|r|n|cffFFFFFFNormal: 100%|r|n|cffFF0000Magic: 35%|r|n|cffFF0000Pierce: 35%|r
ARMORTIP_DIVINE=Damage received from:|n|cff00FF00Magic: 200%|r|n|cffFF0000Normal: 20%|r|n|cffFF0000Pierce: 10%|r|n|cffFF0000Siege: 10%|r
ARMORTIP_NONE=Damage received from:|n|cff00FF00Siege: 200%|r|n|cff00FF00Magic: 150%|r|n|cff00FF00Normal: 150%|r|n|cff00FF00Pierce: 150%|r
ARMOR_DIVINE=Type: |Cffffcc00Spectral|R

DAMAGETIP_MAGIC=Damage against:|n|cff00FF00Large: 200%|r|n|cff00FF00Spectral: 200%|r|n|cff00FF00Unarmored: 150%|r|n|cffFFFFFFSmall: 100%|r|n|cffFF0000Medium: 75%|r|n|cffFF0000Fort: 35%|r
DAMAGETIP_MELEE=Damage against:|n|cff00FF00Medium: 175%|r|n|cff00FF00Unarmored: 150%|r|n|cffFFFFFFLarge: 100%|r|n|cffFFFFFFFort: 100%|r|n|cffFF0000Small: 75%|r|n|cffFF0000Spectral: 20%|r
DAMAGETIP_PIERCE=Damage against:|n|cff00FF00Small: 200%|r|n|cff00FF00Unarmored: 150%|r|n|cffFFFFFFLarge: 100%|r|n|cffFF0000Medium: 75%|r|n|cffFF0000Fort: 35%|r|n|cffFF0000Spectral: 10%|r
DAMAGETIP_SIEGE=Damage against:|n|cff00FF00Fort: 200%|r|n|cff00FF00Unarmored: 200%|r|n|cff00FF00Medium: 150%|r|n|cffFFFFFFSmall: 100%|r|n|cffFFFFFFLarge: 100%|r|n|cffFF0000Spectral: 10%|r

COLON_LUMBER=Blood points:
QUESTSOPTIONAL=Available Modes
RESOURCE_UBERTIP_LUMBER=Blood points are harvested from kills.
RESOURCE_UBERTIP_GOLD=Gold is received after round end.
QUESTS={{ version }}
UPKEEP_NONE=|cffffd700{{ version }}
RESOURCE_UBERTIP_UPKEEP=Released on {{ release_date }}
RESOURCE_UBERTIP_UPKEEP_INFO=|cff00FF00
"""
)


def build_parser():
    # Create the base parser.
    parser = ArgumentParser(
        "Release",
        description="Updates and releases the map based on recent commits.",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )

    # Add the independent arguments.
    parser.add_argument("--version", help="Version to generate, e.g v1.0a.")
    parser.add_argument("--last", help="SHA of the last release.")
    parser.add_argument("--path", help="Path of the project.")
    parser.add_argument("--base", help="Path of the map.")
    parser.add_argument("--repo", help="Name of the repository to update.")
    parser.add_argument("--owner", help="Location of the target repository.")
    parser.add_argument("--remote", help="Name of the corresponding remote.")
    parser.add_argument(
        "--dry-run", help="Disable publishing changes.", action="store_true"
    )

    parser.add_argument("--local", help="Run on local git repository instead of remote", action="store_true")
    # Add the arguments for GitHub credentials.
    parser.add_argument("--token", help="PAT used for GitHub.")
    parser.add_argument("--username", help="Username for GitHub.")
    # login = parser.add_mutually_exclusive_group(required=True)
    # login.add_argument("--token", help="PAT used for GitHub.")
    # login.add_argument("--username", help="Username for GitHub.")

    # Create the argument group used to indicate the version upgrade.
    group = parser.add_mutually_exclusive_group(required=True)
    for part in ["major", "minor", "patch"]:
        group.add_argument(
            f"--{part}", action="store_true", help=f"Upgrade the {part} version."
        )

    # Add the default values.
    parser.set_defaults(
        **{
            "base": "base.w3x",
            "path": ".",
            "remote": "origin",
        }
    )

    # Output the finished parser.
    return parser


# Gets the version of the map, based on the previous release.
def get_version(repo):
    return first(repo.get_releases()).title


# Gets the SHA for the commit for the given version, which is based on the tag.
def get_sha(repo, version):
    for tag in repo.get_tags():
        if tag.name == version:
            return tag.commit.sha


def get_version_from_build():
    # Compute the path of the configuration file.
    path = "wurst.build"

    # Read the build file.
    with open(path) as target:
        build = load(target, Loader=Loader)

    # Look up the previous name of the map.
    name = build["buildMapData"]["name"]
    return search("v{:d}.{:d}{}", name)


# Updates the build file with new version.
def update_build(version):
    # Compute the path of the configuration file.
    path = "wurst.build"

    # Read the build file.
    with open(path) as target:
        build = load(target, Loader=Loader)

    # Look up the previous name of the map.
    name = build["buildMapData"]["name"]

    # Construct the new name for the map.
    name = f"{name.rsplit(maxsplit=1)[0]} {version}"

    # Strip whitespace for the filename to ease access.
    filename = ".".join(name.split())

    # Update the build file.
    build["buildMapData"].update(
        {
            "name": name,
            "fileName": filename,
        }
    )

    # Write the build file.
    with open(path, "w") as target:
        dump(build, target, Dumper=Dumper, sort_keys=False)

    # Output the paths for the build file and built map.
    return path, join("_build", f"{filename}.w3x")


def get_changelog(repo, sha, marker="$changelog: "):
    # Accept abbreviations by allowing partial matches for the SHA.
    def predicate(commit):
        return not commit.sha.startswith(sha)

    # Iterate over the commit history until reaching the given SHA.
    for commit in takewhile(predicate, repo.get_commits()):
        # Consider each line of the commit message separately.
        for line in commit.commit.message.split("\n"):
            # Verify that the line marks a changelog item.
            if line.startswith(marker):
                # Output the changelog message.
                yield line.lstrip(marker).rstrip()

def get_local_changelog(repo, start_sha, end_sha=None, marker="$changelog: "):
    # Get last commit sha of the current branch
    if end_sha == None:
        end_sha = repo.head.object

    # Iterate over commits between start_sha and end_sha
    for commit in repo.iter_commits(rev=f'{start_sha}..{end_sha}'):
        # Consider each line of the commit message separately.
        for line in commit.message.split("\n"):
            # Verify that the line marks a changelog item.
            if line.startswith(marker):
                # Output the changelog message.
                # print(f"Changelog: {line.lstrip(marker).rstrip()}")
                yield line.lstrip(marker).rstrip()

        # print(f"Commit ID: {commit.hexsha}")
        # print(f"Author: {commit.author.name} <{commit.author.email}>")
        # print(f"Commit message: {commit.message}")
        # print(f"Commit date: {commit.authored_datetime}")
        # print()


def write_changelog(major, minor, patch, changelog):
    # Compute the package name.
    package = f"v{major}_{minor:03}_{patch}"

    # Capture the arguments as a dictionary.
    kwargs = locals()

    # Compute the path of the changelog file.
    path = join("wurst", "changelogs", f"{package}.wurst")

    # Construct the path of the file.
    with open(path, "w") as package:
        package.write(changelog_template.render(**kwargs))

    # Output the path for later use.
    return path

def write_war3map_skin(version, release_date):
    kwargs = locals()
    # Compute the path of the changelog file.
    path = join("imports", "war3mapSkin.txt")

    # Construct the path of the file.
    with open(path, "w") as package:
        package.write(war3map_skin_template.render(**kwargs))
    return path

# Extracts the list of WurstScript arguments from the local arguments file.
def get_args():
    # Open the static location.
    with open("wurst_run.args") as args:
        # Filter for lines marking arguments.
        for line in filter(methodcaller("startswith", "-"), args.readlines()):
            # Strip the newline characters.
            yield line.rstrip()


# Build the output map file using `grill` from WurstScript.
def build_map(base, target):
    # Run the command used to build the map
    command = run(
        # Forward the list of arguments from the arguments file.
        ["grill", "build", base, *get_args()],
        # Capture the output to avoid excessive noise.
        capture_output=True,
    )

    # Validate that the build succeeded, independent of the return code.
    if not exists(target):
        exit(f"Wurst build failed: {' '.join(command.args)}")


# Updates the remote using basic git, rather than the GitHub API.
def update_repo(remote, files, version):
    # Construct the repository, based on the working directory.
    repo = Repo()

    # Add all modified files to the index.
    repo.index.add(files)

    # Create the commit.
    commit = repo.index.commit(f"Updated configuration for {version} release.")

    # Push the commit.
    result = repo.remote(remote).push()[0]

    # Validate the result against the 1024 error bit.
    if result.flags & 1 << 10:
        # Undo the latest commit.
        repo.head.reset(commit.parents[0])

        # Notify the user of the failure
        exit(f"Push failure: {result.summary.strip()}")


# Constructs the GitHub repository object based on the local git project.
def get_repo(remote):
    # Fetch the URL for the given remote.
    url = Repo().remote(remote).url

    # List the patterns a GitHub repository URL can assume.
    patterns = [
        "git@github.com:{}/{}.git",
        "https://github.com/{}/{}.git",
    ]

    # Attempt to parse the URL.
    if not (match := first(map(partial(search, string=url), patterns))):
        exit(f"Invalid remote URL: {url}")

    # Construct and output the repository target.
    return "/".join(match)

def find_recent_release_commit(repo):
    releases = [commit for commit in repo.iter_commits() if commit.summary.startswith("Release")]

    if releases:
        most_recent_release = releases[0]
        return most_recent_release
    else:
        return None

if __name__ == "__main__":
    # Create the parser.
    parser = build_parser()

    # Parse the arguments.
    args = parser.parse_args()

    # Update the working directory.
    chdir(args.path)

    sha = ""
    if not args.local:
        # Create the client for GitHub interaction.
        if args.token:
            github = Github(args.token)
        else:
            github = Github(args.username, getpass())
        # Look up the repository.
        repo = github.get_repo(get_repo(args.remote))

        # Fetch the previous version.
        version = get_version(repo)

        # # Fetch the SHA associated with that version.
        sha = args.last or get_sha(repo, version)

        version = args.version
    else:
        repo = Repo(".")
        sha = find_recent_release_commit(repo)

    # Parse the version.
    # major, minor, patch = search("v{:d}.{:d}{}", version)
    major, minor, patch = get_version_from_build()

    # Advance the specified version attribute.
    if args.major:
        major += 1
        minor = 0
        patch = "a"
    # Block the minor version from exceeding three digits.
    elif args.minor and args.minor != 999:
        minor += 1
        patch = "a"
    # Block the patch version from exceeding a lowercase letter.
    elif patch != "z":
        patch = chr(ord(patch) + 1)
    else:
        parser.error("Cannot increment version further.")

    # Update the version.
    version = f"v{major}.{minor}{patch}"

    # Compute the changelog.
    # changelog = sorted(get_changelog(repo, sha))
    changelog = sorted(get_local_changelog(repo, sha))

    # Write the changelog package.
    package = write_changelog(major, minor, patch, changelog)

    # Write the war3mapSkin.txt.
    mapskin = write_war3map_skin(version, date.today().strftime("%d/%m/%Y"))

    # Update the build file for the map.
    build, target = update_build(version)

    # Update the repository with the modified files.
    if args.local:
        build_map(args.base, target)
        # Stage the file for commit
        repo.index.add([package, build, mapskin])

        # Commit the
        commit_message = f'Release v{version}\n' + "\n\* ".join(changelog)
        repo.index.commit(commit_message)
        print("Changelog:", *changelog, sep="\n")
        # Verify that the map can be built.
    elif args.dry_run:
        print("Changelog:", *changelog, sep="\n")
    else:
        # Verify that the map can be built.
        build_map(args.base, target)

        # Push the changes.
        update_repo(args.remote, [package, build, mapskin], version)

        # Release the changes.
        repo.create_git_release(
            tag=version,
            name=version,
            message="\n".join(changelog),
            target_commitish=repo.get_branch("master"),
        ).upload_asset(target)
