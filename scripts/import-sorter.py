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

root_path = "./"

def add_import_line(import_lines, import_files, prefix):
    pkg_list = [import_line.split(".")[0] for import_line in import_lines]
    import_match = [
        imp_filename
        for pkg in pkg_list
        for imp_filename in import_files
        if pkg in imp_filename
    ]
    return prefix + "\n".join(sorted(import_match))

def main():
    """A simple script to re-order package import of wurst files.
    """
    start_time = time.time()

    # Get list of wurst files in current project
    current_project_path = Path(__file__).resolve().parent.parent / "wurst"
    filenames = [
        filename
        for filename in os.listdir(str(current_project_path))
        if filename.endswith(".wurst")
    ]

    for filename in filenames:
        # Open local project wurst files
        with open(current_project_path / filename, "r") as file_to_format:
            lines = file_to_format.readlines()

            # Register import lines
            import_list = [line[:-1] for line in lines if line.startswith("import ")]

            # Register import package name
            package_list = [pkg.split(" ")[-1] for pkg in import_list]

            # Bunch of list to store import lines to order later
            stdlib_list = []
            local_list = []
            third_party_list = []

            # Iterate over every wurst files in the dependencies directory
            for root, _, f_names in os.walk(root_path):
                gen = (f for f in f_names if f.endswith(".wurst"))
                for f in gen:
                    # Check if the file is imported as a package
                    if not f.split(".")[0] in package_list:
                        continue
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


            new_import_section = lines[0].replace("\n", "")

            if len(stdlib_list) > 0:
                new_import_section += "\n" + add_import_line(
                    stdlib_list, import_list, "\n" + import_comments[0] + "\n"
                )

            if len(third_party_list) > 0:
                new_import_section += "\n" + add_import_line(
                    third_party_list, import_list, "\n" + import_comments[1] + "\n"
                )

            if len(local_list) > 0:
                new_import_section += "\n" + add_import_line(
                    local_list, import_list, "\n" + import_comments[2] + "\n"
                )

            file_part = "".join(
                [
                    x
                    for x in lines[2:]
                    if not x.startswith("import")
                    and not (any(comment in x for comment in import_comments))
                ]
            ).lstrip("\n")

            with open(current_project_path / filename, "w") as file:
                # Open the file for writing (creates the file if it doesn't exist)
                # file = open(current_project_path / filenames[0], "w")
                # file = open("example.wurst", "w")

                # Write some text to the file
                file.write(new_import_section + "\n\n" + file_part)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Formatted: {len(filenames)} files in {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
