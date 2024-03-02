import re
import csv
from pathlib import Path


with open(str(Path("wurst/systems/armyHandler/ArmySpawner.wurst")), "r") as file:
    file_contents = file.read()

# Define a regular expression pattern to match "new BTBuildingData" lines with BUILDING_ IDs
pattern = re.compile(
    r"new\s+BTBuildingData\s*\(\s*(BUILDING_[A-Z_]+(?:\s*,\s*BUILDING_[A-Z_]+)*)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*genList\((.*?)\)\s*\)"
)


# Find all matches in the code
matches = pattern.findall(file_contents)

# Iterate through the matches and extract the information
building_data = {}
for match in matches:
    building_id, gold_cost, lumber_cost, unit_list = match
    unit_count = int(unit_list.split(",")[-1])
    building_data[building_id.split(",")[-1].strip()] = {
        "goldCost": int(gold_cost),
        "lumberCost": int(lumber_cost),
        "unitCount": unit_count,
    }


def getAttackData(attack_data: str):
    attack_type, damage, d1, d2, attack_rate = attack_data.split(",")
    min = int(damage)
    max = int(damage) + int(d1) * int(d2)
    dps = round((min + max / 2) / float(attack_rate), 2)
    return {"attackType": attack_type.split(".")[1], "dps": dps, "esperanceDps" : 0}


def getArmorData(armor_data: str):
    armor_type, armor = armor_data.split(",")
    reduction_percent = round((int(armor) * 0.06) / (1 + 0.06 * int(armor)) * 100, 2)
    return {
        "armorType": armor_type.split(".")[1],
        "reductionPercent": reduction_percent,
        "esperanceReductionPercent": 0,
    }


attribute_to_register = {
    "setAttack1Data": getAttackData,
    "setArmorData": getArmorData,
    "setHitPointsMaximumBase": None,
}

# Initialize a list to store extracted attributes
unit_attributes_list = []

def read_unit_attributes(filepath: str):
    # Read the unit definition file
    with open(str(Path(filepath)), "r") as file:
        file_contents = file.read()

    # Define regular expressions for extracting unit attributes
    unit_regex = re.compile(r"createSpawnedUnit\((.*?), (.*?), (.*?)\)")
    function_calls = re.compile(r"\.\.(\w+)\((.*?)\)", re.DOTALL)

    # Find all unit matches
    unit_matches = unit_regex.findall(file_contents)
    for unit_match in unit_matches:
        unit_id, _, building_id = unit_match

        unit_def_pattern = re.compile(
            rf"(?<!\/\/\s)createSpawnedUnit\({unit_id},.*?\)\n((?:(\s*\.\.|\s*ABIL\w+|\s*\)|\s*\/\/).*?\n)*)\s*",
            re.DOTALL,
        )

        unit_def_match = unit_def_pattern.search(file_contents)
        if unit_def_match is None:
            continue
        attribute_matches = function_calls.findall(unit_def_match.group())

        # Requires additional compute
        attr_to_extract = {
            x[0]: x[1]
            for x in attribute_matches
            if x[0] in attribute_to_register.keys()
            and attribute_to_register[x[0]] != None
        }
        attr_final = {
            x[0]: x[1]
            for x in attribute_matches
            if x[0] in attribute_to_register.keys()
            and attribute_to_register[x[0]] == None
        }

        # TODO: build up the attributes, remove attackData1, armorData1...
        for k, v in attr_to_extract.items():
            attr_final.update(attribute_to_register[k](v))

        if building_data.get(building_id) is not None:
            attr_final.update(building_data.get(building_id))

        # Add unit attributes to the list
        unit_attributes_list.append(
            {
                "UnitId": unit_id,
                "BuildingType": building_id,
                **attr_final,
            }
        )


# The following block is executed only if the script is run directly, not if it's imported as a module.
if __name__ == "__main__":
    race_dict = {
        "dps": 0,
        "esperanceDps": 0,
        "attackType": 0,
        "reductionPercent": 0,
        "esperanceReductionPercent": 0,
        "unitCount": 0,
        "goldCost": 0,
        "BuildingType": 0,
        "setHitPointsMaximumBase": 0,
        "lumberCost": 0,
        "armorType": 0,
    }

    unit_attributes_list.append({**{"UnitId": "Human"}, **race_dict})
    read_unit_attributes("wurst/objects/units/HumanUnitsDef.wurst")
    unit_attributes_list.append({**{"UnitId": "Orc"}, **race_dict})
    read_unit_attributes("wurst/objects/units/OrcUnitsDef.wurst")
    unit_attributes_list.append({**{"UnitId": "Undead"}, **race_dict})
    read_unit_attributes("wurst/objects/units/UndeadUnitsDef.wurst")
    unit_attributes_list.append({**{"UnitId": "NightElf"}, **race_dict})
    read_unit_attributes("wurst/objects/units/NightElfUnitsDef.wurst")
    # Define the CSV file and header
    csv_file = "unit_attributes.csv"

    # all_attribute_names = set()
    # for attributes in unit_attributes_list:
    #     all_attribute_names.update(attributes.keys())
    # header.extend(sorted(all_attribute_names))

    minPower = 0

    for row in unit_attributes_list:
        attack_type = row.get("attackType", 0)
        dps = row.get("dps", 0)
        armorType = row.get("armorType", 0)
        reductionPercent = row.get("reductionPercent", 0)
        hitpoint = int(row.get("setHitPointsMaximumBase", 0))
        goldCost = row.get("goldCost", 0)
        lumberCost = row.get("lumberCost", 0)
        unitCount = row.get("unitCount", 1)
        # esperance_value =
        # TODO: faire la médianne pour faire plez a stéphane
        esperance_dps = sum(unit_attr.get('dps', 0) for unit_attr in unit_attributes_list) / (len(unit_attributes_list) - 4)
        esperance_reductionPercent = sum(unit_attr.get('reductionPercent', 0) for unit_attr in unit_attributes_list) / (len(unit_attributes_list) - 4)
        esperance_hitpoint = sum(int(unit_attr.get('setHitPointsMaximumBase', 0)) for unit_attr in unit_attributes_list) / (len(unit_attributes_list) - 4)

        true_dps = dps - esperance_dps
        true_reductionPercent = reductionPercent - esperance_reductionPercent
        true_hitpoint = hitpoint - esperance_hitpoint

        if unitCount > 0:
            power = round((true_dps + true_hitpoint + true_reductionPercent) / unitCount, 0)
            if minPower > power:
                minPower = power
        else:
            power = 0
        # power = round((dps + reductionPercent + goldCost + lumberCost) / 10, 0)
        row.update({"power": power})

        row["esperanceDps"] = esperance_dps
        row["esperanceReductionPercent"] = esperance_reductionPercent
        row.update({"esperance_hitpoint" : esperance_hitpoint})
        # row.update({"powerStacked": round(power * unitCount, 0)})
    unit_attributes_list = [{k: v + abs(minPower) if k == "power" else v for k, v in unit_attr.items()} for unit_attr in unit_attributes_list]

    # Extract all attribute names and add them to the CSV header
    header = list(unit_attributes_list[0].keys())
    
    ############################################################
    # TIS I #
    ############################################################
    
    # Imports, config on pandas's side so it does not pester with false positives warnings and change display settings
    import pandas as pd
    from IPython.display import display
    pd.options.mode.chained_assignment = None
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    
    # Create the dataframe from the csv and begin cleaning the Dataframe
    df = pd.DataFrame(unit_attributes_list)
    df = df.drop(columns=['esperanceDps', 'esperanceReductionPercent', 'esperance_hitpoint', 'power', 'BuildingType'])
    # df.describe(include='all')
    # display(df)
    
    # Code to add the Faction as a new column
    threshold_values = ['Human', 'Orc', 'Undead', 'NightElf']
    currentFaction = ''
    def calculate_new_column_value(row, thresholds):
        global currentFaction
        if row['UnitId'] in thresholds:
            currentFaction = row['UnitId']
            return f"None"
        else:
            return f"{currentFaction}"
    df['Faction'] = df.apply(calculate_new_column_value, args=(threshold_values,), axis=1)
    
    # Finish cleaning of the Dataframe and removing the archmage because it is the only row with Nan values
    df = df.loc[df["Faction"] != 'None']
    df['UnitId'] = df['UnitId'].str[5:]
    df = df.rename(columns= {'UnitId': 'Unit', 'setHitPointsMaximumBase': 'HitPoints'})
    df = df.rename(columns= {'setHitPointsMaximumBase': 'HitPoints'})
    df = df.loc[df["Unit"] != 'ARCHMAGE']
    df = df.astype({"Unit":'category', "dps":'float64', "attackType":'category', "reductionPercent":'float64', "unitCount":'int64', "goldCost":'int64', "HitPoints":'int64', "lumberCost":'int64',
                    "armorType":'category', "Faction":'category'}) 
    
    # Analyses
    df.describe(include='all')
    display(df)
    df.groupby(['armorType', 'Faction']).mean('reductionPercent')
    df.groupby(['armorType', 'Faction']).agg(["mean","count"])
    
    
    ############################################################
    # TIS I #
    ############################################################
    
    # Write unit attributes to the CSV file
    with open(csv_file, "w", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=header)
        csv_writer.writeheader()
        csv_writer.writerows(unit_attributes_list)

    print(f"Unit attributes saved to {csv_file}")
