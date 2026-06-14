import random

base_species: list[str] = ["aasimar", "dragonborn", "dwarf", "elf", "gnome", "goliath", "halfling", "human", "orc", "tiefling"]
eberron_species: list[str] = ["changling", "kalashtar", "khoravar", "shifter", "warforged"]
mythozoology_species: list[str] = ["hoofborn", "inukin", "kappa"]

dragonborn_sub: list[str] = ["black", "blue", "brass", "bronze", "copper", "gold", "green", "red", "silver", "white"]
elf_sub: list[str] = ["drow", "high elf", "wood elf"]
gnome_sub: list[str] = ["forest gnome", "rock gnome"]
goliath_sub: list[str] = ["cloud", "fire", "frost", "hill", "stone", "storm"]
tiefling_sub: list[str] = ["abyssal", "chthonic", "infernal"]
hoofborn_sub: list[str] = ["tidehoof"]
kappa_sub: list[str] = ["wrangler", "tideweaver"]
shifter_sub: list[str] = ["beasthide", "longtooth", "swiftstride", "wildhunt"]

base_classes: list[str] = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]
eberron_classes: list[str] = ["artificer"]

base_barb_sub: list[str] = ["berserker", "wild heart", "world tree", "zealot"]
base_bard_sub: list[str] = ["dance", "glamour", "lore", "valor"]
base_cler_sub: list[str] = ["life", "light", "trickery", "war"]
base_drui_sub: list[str] = ["land", "moon", "sea", "stars"]
base_figh_sub: list[str] = ["battle master", "champion", "eldritch knight", "psi warrior"]
base_monk_sub: list[str] = ["mercy", "shadow", "elements", "open hand"]
base_pala_sub: list[str] = ["devotion", "glory", "ancients", "vengeance"]
base_rang_sub: list[str] = ["beast master", "fey wanderer", "gloom stalker", "hunter"]
base_rogu_sub: list[str] = ["arcane trickster", "assassin", "soulknife", "theif"]
base_sorc_sub: list[str] = ["aberrant", "clockwork", "draconic", "wild magic"]
base_warl_sub: list[str] = ["archfey", "celestial", "fiend", "great old one"]
base_wiza_sub: list[str] = ["abjurer", "diviner", "evoker", "illusionist"]
eberron_arti_sub: list[str] = ["alchemist", "armorer", "artillerist", "battle smith", "cartographer"]

base_background: list[str] = ["acolyte", "artisan", "charlatan", "criminal", "entertainer", "farmer", "guard", "guide", "hermit", "merchant", "noble", "sage", "sailor", "scribe", "soldier", "wayfarer"]
eberron_background: list[str] = ["aberrant heir", "archaeologist", "house agent", "house cannith heir", "house deneith heir", "house ghallanda heir", "house jorasco heir", "house kundarak heir", "house lyrandar heir", "house medani heir", "house orien heir", "house phiarlan heir", "house sivis heir", "house tharashk heir", "house vadalis heir", "inquisitive"]

def class_roll(selected_classes):
    random_class = selected_classes[random.randrange(0, len(selected_classes))]
    if random_class == "barbarian":
        random_sub = base_barb_sub[random.randrange(0, len(base_barb_sub))]
    elif random_class == "bard":
        random_sub = base_bard_sub[random.randrange(0, len(base_bard_sub))]
    elif random_class == "cleric":
        random_sub = base_cler_sub[random.randrange(0, len(base_cler_sub))]
    elif random_class == "druid":
        random_sub = base_drui_sub[random.randrange(0, len(base_drui_sub))]
    elif random_class == "fighter":
        random_sub = base_figh_sub[random.randrange(0, len(base_figh_sub))]
    elif random_class == "monk":
        random_sub = base_monk_sub[random.randrange(0, len(base_monk_sub))]
    elif random_class == "paladin":
        random_sub = base_pala_sub[random.randrange(0, len(base_pala_sub))]
    elif random_class == "ranger":
        random_sub = base_rang_sub[random.randrange(0, len(base_rang_sub))]
    elif random_class == "rogue":
        random_sub = base_rogu_sub[random.randrange(0, len(base_rogu_sub))]
    elif random_class == "sorcerer":
        random_sub = base_sorc_sub[random.randrange(0, len(base_sorc_sub))]
    elif random_class == "warlock":
        random_sub = base_warl_sub[random.randrange(0, len(base_warl_sub))]
    elif random_class == "wizard":
        random_sub = base_wiza_sub[random.randrange(0, len(base_wiza_sub))]
    elif random_class == "artificer":
        random_sub = eberron_arti_sub[random.randrange(0, len(eberron_arti_sub))]
    return random_class.title(), random_sub.title()

def species_roll(selected_species):
    random_species = selected_species[(random.randrange(0, len(selected_species)))]
    if random_species == "dragonborn":
        return f"Dragonborn, {dragonborn_sub[random.randrange(0, len(dragonborn_sub))].title()} Heritage"
    elif random_species == "elf":
        return f"{elf_sub[random.randrange(0, len(elf_sub))].title()}"
    elif random_species == "gnome":
        return f"{gnome_sub[random.randrange(0, len(gnome_sub))].title()}"
    elif random_species == "goliath":
        return f"Goliath, {goliath_sub[random.randrange(0, len(goliath_sub))].title()} Heritage"
    elif random_species == "tiefling":
        return f"{tiefling_sub[random.randrange(0, len(tiefling_sub))].title()} Tiefling"
    elif random_species == "hoofborn":
        return f"{hoofborn_sub[random.randrange(0, len(hoofborn_sub))].title()} Hoofborn"
    elif random_species == "kappa":
        return f"{kappa_sub[random.randrange(0, len(kappa_sub))].title()} Kappa"
    elif random_species == "shifter":
        return f"{shifter_sub[random.randrange(0, len(shifter_sub))].title()} Shifter"
    else:
        return random_species.title()
    
def background_roll(selected_background): 
    random_background = selected_background[random.randrange(0, len(selected_background))]
    return random_background.title()