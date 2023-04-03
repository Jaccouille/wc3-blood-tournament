import os
import re
from pprint import pprint

# Set directory path
model_directory = "/Users/marc/PersonalWork/WurstProject/island-troll-tribes/imports/Models/Units"
icon_directory = "/Users/marc/PersonalWork/WurstProject/island-troll-tribes/imports/ReplaceableTextures/CommandButtons"

def to_camelcase(string, separators=["_", "-", " "]):
    string = string[0].lower() + string[1:]
    for separator in separators:
        if separator in string:
            words = string.split(separator)
            # print(words[0])
            return words[0].lower() + "".join(word.capitalize() for word in words[1:])
    return string


def get_file_paths(directory):
    # Create a list to store file paths
    file_paths = {}
    # Loop through directory and get all file paths
    for root, _, files in os.walk(directory):
        for filename in filter(lambda f: "_portrait" not in f.lower(), files):
            file_path = os.path.join(root, filename)
            key = to_camelcase(filename.split('.')[0])
            file_paths[key] = file_path.split('imports/')[1]
    return file_paths

icon_list = get_file_paths(icon_directory)
model_list = get_file_paths(model_directory)

pprint(icon_list)
pprint(model_list)

# Define the file path and the start and end tokens
file_path = "example.wurst"
start_token = "public class LocalIcons"
end_token = "public class LocalUnits"

# Define the list of replacement strings
replacement_list = ["replacement string 1", "replacement string 2", "replacement string 3"]

def replace_contents(contents, start_token, end_token, replacement_list):
    # Use a regular expression to find the content between the start and end tokens
    pattern = re.compile(start_token + "(.*?)" + end_token, re.DOTALL)
    match = pattern.search(contents)
    if match:
        # Replace the content between the start and end tokens with the replacement strings
        replacement_str = "\n".join(replacement_list)
        contents = contents.replace(match.group(0), start_token + "\n" + replacement_str + "\n\n" + end_token)
    # else:
    #     contents = f"""
    #         package LocalAssets

    #         public class LocalIcons
    #         {test}

    #         public class LocalUnits
    #         {test}
    #     """

def tmp():
    # Read the contents of the file
    with open(file_path, "r") as f:
        contents = f.read()

    # Use a regular expression to find the content between the start and end tokens
    pattern = re.compile(start_token + "(.*?)" + end_token, re.DOTALL)
    match = pattern.search(contents)
    if match:
        # Replace the content between the start and end tokens with the replacement strings
        replacement_str = "\n".join(replacement_list)
        contents = contents.replace(match.group(0), start_token + "\n" + replacement_str + "\n" + end_token)
    else:
        pass
        # icon_list =
        # contents = f"""
        #     package LocalAssets

        #     public class LocalIcons
        #     {test}

        #     public class LocalUnits
        #     {test}
        # """

    # Write the modified contents back to the file
    with open(file_path, "w") as f:
        f.write(contents)
