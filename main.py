import tkinter as tk
from tkinter import ttk



#main window organization
main = tk.Tk()
main.title("D&D Character Randomizer")
main.geometry('900x400')

#geometry control

main.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), uniform = "a")
main.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight = 1, uniform = "a")

#widget creation

class_randomized = ttk.Label(main, text = "cr", background = "pink")
class_label = ttk.Label(main, text = "Class")
class_random_selection = ttk.Button(main, text = "Class Source Options")

subclass_randomized = ttk.Label(main, text = "sr", background = "blue")
subclass_label = ttk.Label(main, text = "Subclass")
subclass_random_selection = ttk.Button(main, text = "Subclass Source Options")

species_randomized = ttk.Label(main, text = "spr", background = "green")
species_label = ttk.Label(main, text = "Species")
species_random_selection = ttk.Button(main, text = "Species Source Options")

background_randomized = ttk.Label(main, text = "bgr", background = "red")
background_label = ttk.Label(main, text = "Background")
background_random_selection = ttk.Button(main, text = "Background Source Options")

stat_gen_label = ttk.Label(main, text = "Stat Generation Selection")
stat_gen_selector = ttk.Button(main)
stat_gen_method = ttk.Label(main, text = "statg")
stats_to_assign = ttk.Label(main, text = "statta")


str_label = ttk.Label(main, text = "Str")
str_stat = ttk.Entry(main)
str_modifier = ttk.Label(main, text = "+0")

dex_label = ttk.Label(main, text = "Dex")
dex_stat = ttk.Entry(main)
dex_modifier = ttk.Label(main, text = "+0")

con_label = ttk.Label(main, text = "Con")
con_stat = ttk.Entry(main)
con_modifier = ttk.Label(main, text = "+0")

int_label = ttk.Label(main, text = "Int")
int_stat = ttk.Entry(main)
int_modifier = ttk.Label(main, text = "+0")

wis_label = ttk.Label(main, text = "Wis")
wis_stat = ttk.Entry(main)
wis_modifier = ttk.Label(main, text = "+0")

cha_label = ttk.Label(main, text = "Cha")
cha_stat = ttk.Entry(main)
cha_modifier = ttk.Label(main, text = "+0")

image_placeholder = ttk.Label(main, text = "Replace with Character Pixel Art", background = "black")

randomize_button = ttk.Button(main, text = "Randomize")
reset_button = ttk.Button(main, text = "Reset Options")
reroll_stats_button = ttk.Button(main, text = "Reroll Stats")

#widget placement

class_randomized.grid(row = 0, column = 0, columnspan = 3, sticky = "nwe")
class_label.grid(row = 1, column = 0, columnspan = 3, sticky = "nwe")
class_random_selection.grid(row = 2, column = 0, columnspan = 3, sticky = "nwe")

subclass_randomized.grid(row = 0, column = 3, columnspan = 3, sticky = "nwe")
subclass_label.grid(row = 1, column = 3, columnspan = 3, sticky = "nwe")
subclass_random_selection.grid(row = 2, column = 3, columnspan=3, sticky = "nwe")

species_randomized.grid(row = 0, column = 6, columnspan = 3, sticky = "nwe")
species_label.grid(row = 1, column = 6, columnspan = 3, sticky = "nwe")
species_random_selection.grid(row = 2, column = 6, columnspan = 3, sticky = "nwe")

background_randomized.grid(row = 0, column = 9, columnspan = 3, sticky = "nwe")
background_label.grid(row = 1, column = 9, columnspan = 3, sticky = "nwe")
background_random_selection.grid(row = 2, column = 9, columnspan = 3, sticky = "nwe")

str_label.grid(row = 4, column = 0, sticky = "nwe")
str_stat.grid(row = 4, column = 1, sticky = "nwe")
str_modifier.grid(row = 4, column = 2, sticky = "nwe")

dex_label.grid(row = 5, column = 0, sticky = "nwe")
dex_stat.grid(row = 5, column = 1, sticky = "nwe")
dex_modifier.grid(row = 5, column = 2, sticky = "nwe")

con_label.grid(row = 6, column = 0, sticky = "nwe")
con_stat.grid(row = 6, column = 1, sticky = "nwe")
con_modifier.grid(row = 6, column = 2, sticky = "nwe")

int_label.grid(row = 7, column = 0, sticky = "nwe")
int_stat.grid(row = 7, column = 1, sticky = "nwe")
int_modifier.grid(row = 7, column = 2, sticky = "nwe")

wis_label.grid(row = 8, column = 0, sticky = "nwe")
wis_stat.grid(row = 8, column = 1, sticky = "nwe")
wis_modifier.grid(row = 8, column = 2, sticky = "nwe")

cha_label.grid(row = 9, column = 0, sticky = "nwe")
cha_stat.grid(row = 9, column = 1, sticky = "nwe")
cha_modifier.grid(row = 9, column = 2, sticky = "nwe")

randomize_button.grid(row = 10, column = 6,  columnspan = 2, sticky = "nwe")
reroll_stats_button.grid(row = 10, column = 8,  columnspan = 2, sticky = "nwe")
reset_button.grid(row = 10, column = 10,  columnspan = 2, sticky = "nwe")

image_placeholder.grid(row = 4, column =6 , rowspan = 6, columnspan = 6, sticky = "nsew")

main.mainloop()