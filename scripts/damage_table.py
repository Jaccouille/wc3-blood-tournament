"""
Author: Jaccouille
Description: This script is used to generate game interface & constant damage tables.
    Just modify the damage_tables dictionary to change the damage values.
    Run the script to update he war3mapMisc.txt and he war3mapMSkin.txt files in
    the imports directory
"""

from itertools import zip_longest
import re

armor_names = {
    "SMALL": "Small",
    "MEDIUM": "Medium",
    "LARGE": "Large",
    "FORT": "Fort",
    "DIVINE": "Spectral",
    "UNKNOWN": "Unknown",
    "NONE": "Unarmored",
}


# Color codes based on damage values
def get_color_code(damage):
    if damage >= 1.5:
        return "|cff00FF00"  # Green
    elif damage < 0.7:
        return "|cffFF0000"  # Red
    elif damage < 1.0:
        return "|cffFFFF00"  # Yellow
    else:
        return "|cffFFFFFF"  # White


def last_number(s):
    # Extract the last number from the string using regular expressions
    matches = re.findall(r"\d+", s)
    if matches:
        return int(matches[-1])  # Convert the last match to an integer
    return 0  # Return 0 if there are no numbers in the string


# Output strings
armor_tips = []
damage_tips = []

# Armor types
armor_types = ["SMALL", "MEDIUM", "LARGE", "FORT", "UNKNOWN", "HERO", "DIVINE", "NONE"]

# Damage types
damage_types = ["MAGIC", "NORMAL", "PIERCE", "SIEGE"]

# Look at the armor_types list for columns/index references
damage_tables = {
    "DamageBonusMagic": [1.00, 0.75, 2.00, 0.35, 1.00, 0.50, 2.00, 1.50],
    "DamageBonusNormal": [0.75, 1.75, 1.00, 1.00, 1.00, 1.00, 0.20, 1.50],
    "DamageBonusPierce": [2.00, 0.75, 1.00, 0.35, 1.00, 0.50, 0.10, 1.50],
    "DamageBonusSiege": [1.00, 1.50, 1.00, 2.00, 1.00, 0.50, 0.10, 2.00],
}


# Generate armor tooltips
for i, armor_type in enumerate(armor_types):
    if armor_type in ["UNKNOWN", "HERO"]:
        continue
    armor_tip = f"ARMORTIP_{armor_type}=Damage received from:"

    armor_percent = []
    for idx, (damage_amount, damage_type) in enumerate(
        zip_longest(damage_tables.values(), damage_types, fillvalue=None)
    ):
        damage_dict = {key: value for key, value in zip(armor_types, damage_amount)}
        color_code = get_color_code(damage_amount[i])
        armor_percent.append(
            f"|n{color_code}{damage_type.capitalize()}: {int(damage_amount[i] * 100)}%|r"
        )
    sorted_list = sorted(armor_percent, key=last_number, reverse=True)
    armor_tips.append(armor_tip + "".join(sorted_list))

# Generate damage tooltips
for i, damage_type in enumerate(damage_types):
    if damage_type == "NORMAL":
        damage_type = "MELEE"
    damage_tip = f"DAMAGETIP_{damage_type}=Damage against:"
    if damage_type == "MELEE":
        damage_type = "NORMAL"
    damage_percent = []

    for j, armor_type in enumerate(armor_types):
        if armor_type in ["UNKNOWN", "HERO"]:
            continue
        damage_bonus = damage_tables[f"DamageBonus{damage_type.capitalize()}"]
        color_code = get_color_code(damage_bonus[j])
        damage_percent.append(
            f"|n{color_code}{armor_names[armor_type].capitalize()}: {int(damage_bonus[j] * 100)}%|r"
        )
    sorted_list = sorted(damage_percent, key=last_number, reverse=True)
    damage_tips.append(damage_tip + "".join(sorted_list))

armor_tips_formatted = "\n".join(armor_tips)
damage_tips_formatted = "\n".join(damage_tips)
war3map_skin_template = """[CustomSkin]
InfoPanelIconArmorDivine=UI\Widgets\Console\Human\infocard-armor-spectral.dds

[FrameDef]
{armor_tips}
ARMOR_DIVINE=Type: |Cffffcc00Spectral|R

{damage_tips}

COLON_LUMBER=Blood points:
RESOURCE_UBERTIP_LUMBER=Blood point are harvested from kills.
""".format(
    armor_tips=armor_tips_formatted,
    damage_tips=damage_tips_formatted,
)

war3map_skin_path = "imports/war3mapSkin.txt"
# Write the modified contents back to the file
with open(war3map_skin_path, "w") as f:
    f.write(war3map_skin_template)

# Convert the dictionary to the desired string format
damage_table_str = ""
for key, values in damage_tables.items():
    damage_table_str += f"{key}=" + ",".join(map(str, values)) + "\n"

war3map_misc_template = """[Misc]
ConstructionRefundRate=1.0
{damage_table_str}
DamageBonusSpells=1.00,1.00,1.00,1.00,1.00,0.75,1.00,1.00
MaxUnitSpeed=522.0
UpgradeRefundRate=1.0
ItemStackingEnabled=1
DefendDeflection=1
BoneDecayTime=15
""".format(
    damage_table_str=damage_table_str
)

war3map_misc_path = "imports/war3mapMisc.txt"
# Write the modified contents back to the file
with open(war3map_misc_path, "w") as f:
    f.write(war3map_misc_template)
