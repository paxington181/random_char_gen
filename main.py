import tkinter as tk
from tkinter import ttk



#main window organization
main = tk.Tk()
main.title("D&D Character Randomizer")
main.geometry('600x400')

#widget creation

class_label = ttk.Label(main, text = "Class")
class_random_selection = ttk.Button(main, text = "Class Source Options")
class_randomized = ttk.Label(main, text = "")

subclass_label = ttk.Label(main, text = "Subclass")
subclass_random_selection = ttk.Button(main, text = "Subclass Source Options")
subclass_randomized = ttk.Label(main, text = "")

species_label = ttk.Label(main, text = "Species")
species_random_selecction = ttk.Button(main, text = "Species Source Options")
species_randomized = ttk.Label(main, text = "")

background_label = ttk.Label(main, text = "Background")
background_random_selection = ttk.Button(main, text = "Background Source Options")
background_randomized = ttk.Label(main, text = "")


str_label = ttk.Label(main, text = "Str")
str_stat = ttk.Entry(main)
str_modifier = ttk.Label(main, text = "")

dex_label = ttk.Label(main, text = "Dex")
dex_stat = ttk.Entry(main)
dex_modifier = ttk.Label(main, text = "")

con_label = ttk.Label(main, text = "Con")
con_stat = ttk.Entry(main)
con_modifier = ttk.Label(main, text = "")

int_label = ttk.Label(main, text = "Int")
int_stat = ttk.Entry(main)
int_modifier = ttk.Label(main, text = "")

wis_label = ttk.Label(main, text = "Wis")
wis_stat = ttk.Entry(main)
wis_modifier = ttk.Label(main, text = "")

cha_label = ttk.Label(main, text = "Cha")
cha_stat = ttk.Entry(main)
cha_modifier = ttk.Label(main, text = "")

image_placeholder = ttk.Label(main, text = "Replace with Character Pixel Art")

randomize_button = ttk.Button(main, text = "Randomize")
reset_button = ttk.Button(main, text = "Reset all options")

#widget placement


main.mainloop()