import random

phb: list[str] = ["acolyte", "artisan", "charlatan", "criminal", "entertainer", "farmer", "guard", "guide", "hermit", "merchant", "noble", "sage", "sailor", "scribe", "soldier", "wayfarer"]
eberron: list[str] = ["aberrant heir", "archaeologist", "house agent", "house cannith heir", "house deneith heir", "house ghallanda heir", "house jorasco heir", "house kundarak heir", "house lyrandar heir", "house medani heir", "house orien heir", "house phiarlan heir", "house sivis heir", "house tharashk heir", "house vadalis heir", "inquisitive"]
ravenloft: list[str] = ["haunted one", "investigator", "mist wanderer", "spirit medium"]


def background_roll(selected_books):
    selected_background = []
    for book in selected_books:
        if book == "2024 PHB":
            selected_background.append(phb)
        elif book == "Eberron":
            selected_background.append(eberron)
        elif book == "Ravenloft":
            selected_background.append(ravenloft)
    if len(selected_background) != 0:
        selected_background = [string for sublist in selected_background for string in sublist]
    else:
        selected_background = phb
    random_background = selected_background[random.randrange(0, len(selected_background))]
    return random_background.title()