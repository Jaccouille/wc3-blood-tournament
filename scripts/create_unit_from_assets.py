"""
Author: Jaccouille
Description: This script is used to generate a LocalAssets.wurst file based on
    the content of /imports directory.
"""

import os
import re
from pprint import pprint
from pathlib import Path
from string import Template
import string

model_directory_path = Path(__file__).resolve().parent.parent / "imports/Models"
icon_directory_path = (
    Path(__file__).resolve().parent.parent / "imports/ReplaceableTextures"
)


def to_camelcase(string, separators=["_", "-", " "]):
    string = string[0].lower() + string[1:]
    for separator in separators:
        if separator in string:
            words = string.split(separator)
            return words[0].lower() + "".join(word.capitalize() for word in words[1:])
    return string


def get_import_file_paths(directory):
    # Create a list to store file paths
    file_paths = {}
    # Loop through directory and get all file paths
    for root, _, files in os.walk(directory):
        for filename in filter(lambda f: "_portrait" not in f.lower(), files):
            file_path = os.path.join(root, filename)
            if "(1)" in filename:
                continue
            key = to_camelcase(filename.split(".")[0])
            key = key.translate(str.maketrans("", "", "()-"))
            file_paths[key] = file_path.split("imports\\")[1]
    return file_paths


icon_pattern = r"(?<=public class LocalIcons\n)[\s\S]*?(?=\n\n|$)"
model_pattern = r"(?<=public class LocalUnits\n)[\s\S]*?(?=\n\n|$)"

template_string = '''    static constant $key = "$file_path"'''
template = Template(template_string)


def replace_section(pattern, replacement_list, contents, prefix=""):
    for match in re.finditer(pattern, contents, re.DOTALL):
        start_index = match.start()
        end_index = match.end()
        print(
            f"Match found at indices {start_index}-{end_index}:\n '{contents[start_index:end_index]}'"
        )
        return (
            contents[:start_index]
            + prefix
            + "\n".join(replacement_list)
            + contents[end_index:]
        )
    print("No match found")
    return contents


def replace_contents(pattern, contents, list_of_replacements):
    new_contents = replace_section(pattern, list_of_replacements, contents)
    return new_contents


def createUnitDefinition(model_list):
    template_string = Template(
        """
    new UnitDefinition(UNIT_ID_GEN.next(), 'hrif')

        ..setModelFile($model)
        ..setName("$name")\n
        """
    )
    str = "package UnitDef\n\nimport UnitObjEditing\nimport ObjectIdGenerator\nimport LocalAssets\n\n@compiletime function createUnits()"
    for k, v in model_list.items():
        name = re.sub(r"(?<!^)(?=[A-Z])", " ", k)
        model = f"LocalUnits.{k}"
        str += template_string.substitute(name=name, model=model)
        pass
    return str


def main():
    # Read the contents of the file
    # file_path = Path(__file__).resolve().parent / "AssetsOutput.wurst"
    file_path = (
        Path(__file__).resolve().parent.parent / "wurst/assets/LocalAssets.wurst"
    )
    unit_def_path = Path(__file__).resolve().parent / "UnitDef.wurst"

    contents = "package AssetsOutput\n\npublic class LocalIcons\n\npublic class LocalUnits\nplaceholder"
    if file_path.exists():
        with open(file_path, "r") as f:
            contents = f.read().rstrip("\n")

    icon_list = get_import_file_paths(icon_directory_path)
    print(icon_list)
    icon_lines = [
        template.substitute(key=key, file_path=icon_list[key]).replace("\\", "/")
        for key in icon_list
    ]
    contents = replace_contents(icon_pattern, contents, icon_lines)

    model_list = get_import_file_paths(model_directory_path)
    model_lines = [
        template.substitute(key=key, file_path=model_list[key]).replace("\\", "/")
        for key in model_list
    ]
    print(model_lines)
    contents = replace_contents(model_pattern, contents, model_lines)

    unit_def_content = createUnitDefinition(model_list)

    # Write the modified contents back to the file
    with open(file_path, "w") as f:
        f.write(contents)

    # To avoid unit def creation
    return
    # Write the modified contents back to the file
    with open(unit_def_path, "w") as f:
        f.write(unit_def_content)


if __name__ == "__main__":
    main()
