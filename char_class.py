import random

phb: list[str] = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]
eberron: list[str] = ["artificer"]

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
ravenloft_arti_sub: list[str] = ["reanimator"]
ravenloft_bard_sub: list[str] = ["spirits"]
ravenloft_cler_sub: list[str] = ["grave"]
ravenloft_rang_sub: list[str] = ["hollow warden"]
ravenloft_rogu_sub: list[str] = ["phantom"]
ravenloft_sorc_sub: list[str] = ["shadow sorcery"]
ravenloft_warl_sub: list[str] = ["undead patron"]

def class_roll(class_books, subclass_books):
    selected_classes = []
    arti_sub = []
    barb_sub = []
    bard_sub = []
    cler_sub = []
    drui_sub = []
    figh_sub = []
    monk_sub = []
    pala_sub = []
    rang_sub = []
    rogu_sub = []
    sorc_sub = []
    warl_sub = []
    wiza_sub = []
    for book in class_books:
        if book == "2024 PHB":
            selected_classes.append(phb)
        elif book == "Eberron":
            selected_classes.append(eberron)
    for book in subclass_books:
        if book == "2024 PHB":
            barb_sub.append(base_barb_sub)
            bard_sub.append(base_bard_sub)
            cler_sub.append(base_cler_sub)
            drui_sub.append(base_drui_sub)
            figh_sub.append(base_figh_sub)
            monk_sub.append(base_monk_sub)
            pala_sub.append(base_pala_sub)
            rang_sub.append(base_rang_sub)
            rogu_sub.append(base_rogu_sub)
            sorc_sub.append(base_sorc_sub)
            warl_sub.append(base_warl_sub)
            wiza_sub.append(base_wiza_sub)
        elif book == "Eberron":
            arti_sub.append(eberron_arti_sub)
        elif book == "Ravenloft":
            arti_sub.append(ravenloft_arti_sub)
            bard_sub.append(ravenloft_bard_sub)
            cler_sub.append(ravenloft_cler_sub)
            rang_sub.append(ravenloft_rang_sub)
            rogu_sub.append(ravenloft_rogu_sub)
            sorc_sub.append(ravenloft_sorc_sub)
            warl_sub.append(ravenloft_warl_sub)
    if len(selected_classes) != 0:
        selected_classes = [string for sublist in selected_classes for string in sublist]
    else:
        selected_classes = phb
    if len(arti_sub) != 0:
        arti_sub = [string for sublist in arti_sub for string in sublist]
    else:
        arti_sub = eberron_arti_sub
    if len(barb_sub) != 0:
        barb_sub = [string for sublist in barb_sub for string in sublist]
    else:
        barb_sub = base_barb_sub
    if len(bard_sub) != 0:
        bard_sub = [string for sublist in bard_sub for string in sublist]
    else:
        bard_sub = base_bard_sub
    if len(cler_sub) != 0:
        cler_sub = [string for sublist in cler_sub for string in sublist]
    else:
        cler_sub = base_cler_sub
    if len(drui_sub) != 0:
        drui_sub = [string for sublist in drui_sub for string in sublist]
    else:
        drui_sub = base_drui_sub
    if len(figh_sub) != 0:
        figh_sub = [string for sublist in figh_sub for string in sublist]
    else:
        figh_sub = base_figh_sub
    if len(monk_sub) != 0:
        monk_sub= [string for sublist in monk_sub for string in sublist]
    else:
        monk_sub = base_monk_sub
    if len(pala_sub) != 0:
        pala_sub = [string for sublist in pala_sub for string in sublist]
    else:
        pala_sub = base_pala_sub
    if len(rang_sub) != 0:
        rang_sub = [string for sublist in rang_sub for string in sublist]
    else:
        rang_sub = base_rang_sub
    if len(rogu_sub) != 0:
        rogu_sub = [string for sublist in rogu_sub for string in sublist]
    else:
        rogu_sub = base_rogu_sub
    if len(sorc_sub) != 0:
        sorc_sub = [string for sublist in sorc_sub for string in sublist]
    else:
        sorc_sub = base_sorc_sub
    if len(warl_sub) != 0:
        warl_sub = [string for sublist in warl_sub for string in sublist]
    else:
        warl_sub = base_warl_sub
    if len(wiza_sub) != 0:
        wiza_sub = [string for sublist in wiza_sub for string in sublist]
    else:
        wiza_sub = base_wiza_sub
    random_class = selected_classes[random.randrange(0, len(selected_classes))]
    if random_class == "barbarian":
        random_sub = barb_sub[random.randrange(0, len(barb_sub))]
        return f"Path of the {random_sub.title()} Barbarian"
    elif random_class == "bard":
        random_sub = bard_sub[random.randrange(0, len(bard_sub))]
        return f"College of {random_sub.title()} Bard"
    elif random_class == "cleric":
        random_sub = cler_sub[random.randrange(0, len(bard_sub))]
        return f"{random_sub.title()} Domain Cleric"
    elif random_class == "druid":
        random_sub = drui_sub[random.randrange(0, len(drui_sub))]
        return f"Circle of the {random_sub.title()} Druid"
    elif random_class == "fighter":
        random_sub = figh_sub[random.randrange(0, len(figh_sub))]
        return f"{random_sub.title()} Fighter"
    elif random_class == "monk":
        random_sub = monk_sub[random.randrange(0, len(monk_sub))]
        return f"Warrior of {random_sub.title()} Monk"
    elif random_class == "paladin":
        random_sub = pala_sub[random.randrange(0, len(pala_sub))]
        return f"Oath of {random_sub.title()} Paladin"
    elif random_class == "ranger":
        random_sub = rang_sub[random.randrange(0, len(rang_sub))]
        return f"{random_sub.title()} Ranger"
    elif random_class == "rogue":
        random_sub = rogu_sub[random.randrange(0, len(rogu_sub))]
        return f"{random_sub.title()} Rogue"
    elif random_class == "sorcerer":
        random_sub = sorc_sub[random.randrange(0, len(sorc_sub))]
        return f"{random_sub.title()} Sorcery Sorcerer"
    elif random_class == "warlock":
        random_sub = warl_sub[random.randrange(0, len(warl_sub))]
        return f"Pact of the {random_sub.title()} Warlock"
    elif random_class == "wizard":
        random_sub = wiza_sub[random.randrange(0, len(wiza_sub))]
        return f"{random_sub.title()} Wizard"
    elif random_class == "artificer":
        random_sub = arti_sub[random.randrange(0, len(arti_sub))]
        return f"{random_sub.title()} Artificer"
