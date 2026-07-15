import random

phb: list[str] = ["aasimar", "dragonborn", "dwarf", "elf", "gnome", "goliath", "halfling", "human", "orc", "tiefling"]
eberron: list[str] = ["changling", "kalashtar", "khoravar", "shifter", "warforged"]
#mythozoology_species: list[str] = ["hoofborn", "inukin", "kappa"]
ravenloft: list[str] = ["dhampir", "hexblood", "lupin", "reborn"]

dragonborn_sub: list[str] = ["black", "blue", "brass", "bronze", "copper", "gold", "green", "red", "silver", "white"]
elf_sub: list[str] = ["drow", "high elf", "wood elf"]
gnome_sub: list[str] = ["forest gnome", "rock gnome"]
goliath_sub: list[str] = ["cloud", "fire", "frost", "hill", "stone", "storm"]
tiefling_sub: list[str] = ["abyssal", "chthonic", "infernal"]
#hoofborn_sub: list[str] = ["tidehoof"]
#kappa_sub: list[str] = ["wrangler", "tideweaver"]
shifter_sub: list[str] = ["beasthide", "longtooth", "swiftstride", "wildhunt"]


def species_roll(selected_books):
    selected_species = []
    for book in selected_books:
        if book == "2024 PHB":
            selected_species.append(phb)
        elif book == "Eberron":
            selected_species.append(eberron)
        elif book == "Ravenloft":
            selected_species.append(ravenloft)
    if len(selected_species) != 0:
        selected_species = [string for sublist in selected_species for string in sublist]
    else:    
        selected_species = phb
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
    # elif random_species == "hoofborn":
    #     return f"{hoofborn_sub[random.randrange(0, len(hoofborn_sub))].title()} Hoofborn"
    # elif random_species == "kappa":
    #     return f"{kappa_sub[random.randrange(0, len(kappa_sub))].title()} Kappa"
    elif random_species == "shifter":
        return f"{shifter_sub[random.randrange(0, len(shifter_sub))].title()} Shifter"
    else:
        return random_species.title()