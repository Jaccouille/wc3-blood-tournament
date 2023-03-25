import io
import os
from os import path
from collections import defaultdict
import re
from pprint import pprint

def main():
    properties_path = "/Users/marc/PersonalWork/WurstProject/wc3-blood-tournament/wurst/"
    filenames = [
            filename
            for filename in os.listdir(properties_path)
            if filename.endswith(".wurst")
        ]

    pattern = re.compile(r"^[a-zA-z\.]+=")
    setList = []

    path = "./"

    with open(properties_path + filenames[0], 'r') as f:
        lines = f.readlines()
        import_list = []
        package_list = []
        for line in lines:
            if line.startswith("import "):
                import_list.append(line[:-1])
        for imp in import_list:
            package_name = imp.split(' ')[-1] + ".wurst"
            package_list.append(package_name)
            # print(package_name + ".wurst")

        # print(*package_list, sep='\n')

        stdlib_list = []
        local_list = []
        third_party_list = []

        stdlib_path = "/dependencies/wurstStdlib2/"
        third_party_path = "/dependencies/"

        for root, d_names,f_names in os.walk(path):
            gen = (f for f in f_names if f.endswith(".wurst"))
            for f in gen:
                if f in package_list:
                    print(os.path.join(root, f))
            # if pattern.match(f):
            #     setList.append(root + d_names + package_name + ".wurst")
            # match = [root + d_names + package_name + ".wurst" for f in f_names if package_name + ".wurst" in f]
            # if len(match) > 0:
            #     print(match)

if __name__ == "__main__":
    main()

