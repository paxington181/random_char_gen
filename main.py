import random

base_species: str = ["aasimar", "dragonborn", "dwarf", "elf", "gnome", "goliath", "halfling", "human", "orc", "tiefling"]
eberron_species: str = ["changling", "kalashtar", "khoravar", "shifter", "warforged"]
mythozoology_species: str = ["hoofborn", "inukin", "kappa"]


dragonborn_sub: str = ["black", "blue", "brass", "bronze", "copper", "gold", "green", "red", "silver", "white"]
elf_sub: str = ["drow", "high elf", "wood elf"]
gnome_sub: str = ["forest gnome", "rock gnome"]
goliath_sub: str = ["cloud", "fire", "frost", "hill", "stone", "storm"]
tiefling_sub: str = ["abyssal", "chthonic", "infernal"]
hoofborn_sub: str = ["tidehoof"]
kappa_sub: str = ["wrangler", "tideweaver"]

base_classes: str = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]
eberron_classes: str = ["artificer"]


base_background: str = ["acolyte", "artisan", "charlatan", "criminal", "entertainer", "farmer", "guard", "guide", "hermit", "merchant", "noble", "sage", "sailor", "scribe", "soldier", "wayfarer"]
eberron_background: str = ["aberrant heir", "archaeologist", "house agent", "house cannith heir", "house deneith heir", "house ghallanda heir", "house jorasco heir", "house kundarak heir", "house lyrandar heir", "house medani heir", "house orien heir", "house phiarlan heir", "house sivis heir", "house tharashk heir", "house vadalis heir", "inquisitive"]



def main():
    
    selected_species = base_species + eberron_species + mythozoology_species
    random_species = selected_species[(random.randrange(0, (len(selected_species) - 1 )))]
    print(f"Species selected: {random_species.title()}")


    selected_classes = base_classes + eberron_classes
    random_class = selected_classes[random.randrange(0, (len(selected_classes) - 1))]
    print(f"Class selected: {random_class.title()}")
    
    selected_background = base_background + eberron_background
    random_background = selected_background[random.randrange(0, (len(selected_background) - 1))]
    print(f"Background selected: {random_background.title()}")


main()