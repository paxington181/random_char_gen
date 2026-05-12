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

alignment: str = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]

def stat_roll():
    four_rolls = []
    for i in range(0, 4):
        four_rolls.append(random.randrange(1, 7))
        i += 1
    four_sorted = sorted(four_rolls)
    four_flipped = four_sorted[::-1]
    three_rolls = four_flipped[:3]
    print(three_rolls)
    rolls_sum = sum(three_rolls)
    print(rolls_sum)
    return rolls_sum


def main():
    
    selected_species = base_species + eberron_species + mythozoology_species
    random_species = selected_species[(random.randrange(0, len(selected_species)))]
    if random_species == "dragonborn":
        print(f"Species selected: Dragonborn, {dragonborn_sub[random.randrange(0, len(dragonborn_sub))].title()} dragon ancestry")
    elif random_species == "elf":
        print(f"Species selected: {elf_sub[random.randrange(0, len(elf_sub))].title()}")
    elif random_species == "gnome":
        print(f"Species selected: {gnome_sub[random.randrange(0, len(gnome_sub))].title()}")
    elif random_species == "goliath":
        print(f"Species selected: Goliath, {goliath_sub[random.randrange(0, len(goliath_sub))].title()} Giant ancestry")
    elif random_species == "tiefling":
        print(f"Species selected: {tiefling_sub[random.randrange(0, len(tiefling_sub))].title()} descent Tiefling")
    elif random_species == "hoofborn":
        print(f"Species selected: {hoofborn_sub[random.randrange(0, len(hoofborn_sub))].title()} Hoofborn")
    elif random_species == "kappa":
        print(f"Species selected: {kappa_sub[random.randrange(0, len(kappa_sub))].title()} Kappa")
    else:
        print(f"Species selected: {random_species.title()}")


    selected_classes = base_classes + eberron_classes
    random_class = selected_classes[random.randrange(0, len(selected_classes))]
    print(f"Class selected: {random_class.title()}")
    
    selected_background = base_background + eberron_background
    random_background = selected_background[random.randrange(0, len(selected_background))]
    print(f"Background selected: {random_background.title()}")

    stats_sum: int = []
    for i in range(0, 6):
        stats_sum.append(stat_roll())
        i += 1

    sum_stats = sum(stats_sum)
    sum_rounded:float = round((sum_stats / 72), 2)
        

    print(f"The sum of your stats: {sum(stats_sum)}")
    print(f"The sum of rolled stats are {int(sum_rounded * 100)}% of the sum of the standard array.")
    
    random_alignment = alignment[random.randrange(0, len(alignment))]
    print(f"Alignment selected: {random_alignment}")

main()