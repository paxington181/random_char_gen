import tkinter as tk
from tkinter import ttk



#main window organization
main = tk.Tk()
main.title("D&D Character Randomizer")
main.geometry('1000x400')

#geometry control

main.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), uniform = "a")
main.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight = 1, uniform = "a")

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


str_label = ttk.Label(main, text = "Str", background = "brown")
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

image_placeholder = ttk.Label(main, text = "Replace with Character Pixel Art")

randomize_button = ttk.Button(main, text = "Randomize")
reset_button = ttk.Button(main, text = "Reset all options")

#widget placement

class_randomized.grid(row = 0, column = 0, columnspan=3, sticky = "nwe")
class_label.grid(row = 1, column = 0, columnspan=3, sticky = "nwe")
class_random_selection.grid(row = 2, column = 0, columnspan=3, sticky = "nwe")

subclass_randomized.grid(row = 0, column = 3, columnspan=3, sticky = "nwe")
subclass_label.grid(row = 1, column = 3, columnspan=3, sticky = "nwe")
subclass_random_selection.grid(row = 2, column = 3, columnspan=3, sticky = "nwe")

species_randomized.grid(row = 0, column = 6, columnspan=3, sticky = "nwe")
species_label.grid(row = 1, column = 6, columnspan=3, sticky = "nwe")
species_random_selection.grid(row = 2, column = 6, columnspan=3, sticky = "nwe")

background_randomized.grid(row = 0, column = 9, columnspan=3, sticky = "nwe")
background_label.grid(row = 1, column = 9, columnspan=3, sticky = "nwe")
background_random_selection.grid(row = 2, column = 9, columnspan=3, sticky = "nwe")

str_label.grid(row = 4, column = 0, sticky = "nwe")
str_stat.grid(row = 4, column = 1, sticky = "nwe")
str_modifier.grid(row = 4, column = 2, sticky = "nwe")


main.mainloop()