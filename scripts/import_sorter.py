"""
Author: Jaccouille
Description: This script is used to alphabetically sort Wurst file import.
    // Standard libs imports:
        standardLibPackage
    // Third party imports:
        a package from a dependency for example
    // Local imports:
        your wurst project package
"""

import os
from pathlib import Path
from pprint import pprint
import time

stdlib_path = str(Path("/dependencies/wurstStdlib2/"))
third_party_path = str(Path("/dependencies/"))
import_comments = [
    "// Standard libs imports:",
    "// Third party imports:",
    "// Local imports:",
]

# Bunch of list to store import lines to order later
stdlib_list = []
local_list = []
third_party_list = []

root_path = "./"


def add_import_line(import_files, import_lines, header):
    pkg_list = [import_file.split(".")[0] for import_file in import_files]
    import_match = [f for f in import_lines if f.split(" ")[-1] in pkg_list]
    # [
    #     imp_filename
    #     for pkg in pkg_list
    #     for imp_filename in import_lines
    #     if pkg in imp_filename
    # ]
    if len(import_match) == 0:
        return ""
    return header + "\n".join(sorted(import_match)) + "\n"


def get_wurst_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".wurst"):
                file_list.append(os.path.join(root, file))
    return file_list


def register_project_package():
    # Iterate over every wurst files in the dependencies directory
    for root, _, f_names in os.walk(root_path):
        gen = (f for f in f_names if f.endswith(".wurst"))
        for f in gen:
            complete_path = os.path.join(root, f)
            package_name = f

            # register package from stdlib
            if stdlib_path in complete_path:
                stdlib_list.append(package_name)

            # register package from third party dependencies
            elif third_party_path in complete_path:
                third_party_list.append(package_name)

            # register package from local project
            else:
                local_list.append(package_name)


def main():
    """A simple script to re-order package import of wurst files."""
    start_time = time.time()

    # Get list of wurst files in current project
    current_project_path = Path(__file__).resolve().parent.parent / "wurst"
    filenames = [
        filename
        for filename in os.listdir(str(current_project_path))
        if filename.endswith(".wurst")
    ]

    wurst_files = get_wurst_files(str(current_project_path))
    register_project_package()

    for wurst_file_path in wurst_files:
        # Open local project wurst files
        with open(wurst_file_path, "r") as file_to_format:
            lines = file_to_format.readlines()
            filename = os.path.basename(wurst_file_path)

            # Register import lines
            import_lines = [line[:-1] for line in lines if line.startswith("import ")]

            # Register import package name
            package_list = [pkg.split(" ")[-1] for pkg in import_lines]

            new_import_section = lines[0].replace("\n", "") + "\n"
            if len(import_lines) == 0:
                continue
            new_import_section += add_import_line(
                stdlib_list, import_lines, "\n" + import_comments[0] + "\n"
            )

            new_import_section += add_import_line(
                third_party_list, import_lines, "\n" + import_comments[1] + "\n"
            )

            new_import_section += add_import_line(
                local_list, import_lines, "\n" + import_comments[2] + "\n"
            )

            file_part = "".join(
                [
                    x
                    for x in lines[2:]
                    if not x.startswith("import")
                    and not (any(comment in x for comment in import_comments))
                ]
            ).lstrip("\n")

            with open(wurst_file_path, "w") as file:
                # Open the file for writing (creates the file if it doesn't exist)
                # file = open(current_project_path / filenames[0], "w")
                # file = open("example.wurst", "w")

                # Write some text to the file
                file.write(new_import_section.rstrip(("\n")) + "\n\n" + file_part)
                print("Processed " + file.name)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Formatted: {len(wurst_files)} files in {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
