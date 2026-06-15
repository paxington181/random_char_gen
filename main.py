import tkinter as tk
from tkinter import Listbox
from tkinter import PhotoImage
from tkinter import ttk
from stat_rolling import tdsix_set, fdsix_set, mdsix_set
from cssb import *

selected_classes = base_classes
selected_species = base_species
selected_backgrounds = base_background


def update_all():
    rclass, rsub = class_roll(selected_classes)
    class_randomized.configure(text = f"{rclass}")
    subclass_randomized.configure(text = f"{rsub}")
    rspec = species_roll(selected_species)
    species_randomized.configure(text = f"{rspec}")
    rback = background_roll(selected_backgrounds)
    background_randomized.configure(text = f"{rback}")

def roll_stats_standard():
    current_stats = [15, 14, 13, 12, 10, 8]
    stats_rolls_one.configure(text = f"{current_stats[0]}")
    stats_sum_one.configure(text = f"{current_stats[0]}")
    stats_rolls_two.configure(text = f"{current_stats[1]}")
    stats_sum_two.configure(text = f"{current_stats[1]}")
    stats_rolls_three.configure(text = f"{current_stats[2]}")
    stats_sum_three.configure(text = f"{current_stats[2]}")
    stats_rolls_four.configure(text = f"{current_stats[3]}")
    stats_sum_four.configure(text = f"{current_stats[3]}")
    stats_rolls_five.configure(text = f"{current_stats[4]}")
    stats_sum_five.configure(text = f"{current_stats[4]}")
    stats_rolls_six.configure(text = f"{current_stats[5]}")
    stats_sum_six.configure(text = f"{current_stats[5]}")
    stats_total.configure(text = f" {sum(current_stats)}")
    stats_percent.configure(text = f" {int(round((sum(current_stats) / 72), 2) * 100)}%")

def roll_stats_tdsix():
    current_stats = tdsix_set()
    stats_rolls_one.configure(text = f"{current_stats[0][1:]}")
    stats_sum_one.configure(text = f"{current_stats[0][0]}")
    stats_rolls_two.configure(text = f"{current_stats[1][1:]}")
    stats_sum_two.configure(text = f"{current_stats[1][0]}")
    stats_rolls_three.configure(text = f"{current_stats[2][1:]}")
    stats_sum_three.configure(text = f"{current_stats[2][0]}")
    stats_rolls_four.configure(text = f"{current_stats[3][1:]}")
    stats_sum_four.configure(text = f"{current_stats[3][0]}")
    stats_rolls_five.configure(text = f"{current_stats[4][1:]}")
    stats_sum_five.configure(text = f"{current_stats[4][0]}")
    stats_rolls_six.configure(text = f"{current_stats[5][1:]}")
    stats_sum_six.configure(text = f"{current_stats[5][0]}")
    stats_total.configure(text = f" {current_stats[6]}")
    stats_percent.configure(text = f" {int(round((current_stats[6] / 72), 2) * 100)}%")

def roll_stats_fdsix():
    current_stats = fdsix_set()
    stats_rolls_one.configure(text = f"{current_stats[0][1:]}")
    stats_sum_one.configure(text = f"{current_stats[0][0]}")
    stats_rolls_two.configure(text = f"{current_stats[1][1:]}")
    stats_sum_two.configure(text = f"{current_stats[1][0]}")
    stats_rolls_three.configure(text = f"{current_stats[2][1:]}")
    stats_sum_three.configure(text = f"{current_stats[2][0]}")
    stats_rolls_four.configure(text = f"{current_stats[3][1:]}")
    stats_sum_four.configure(text = f"{current_stats[3][0]}")
    stats_rolls_five.configure(text = f"{current_stats[4][1:]}")
    stats_sum_five.configure(text = f"{current_stats[4][0]}")
    stats_rolls_six.configure(text = f"{current_stats[5][1:]}")
    stats_sum_six.configure(text = f"{current_stats[5][0]}")
    stats_total.configure(text = f" {current_stats[6]}")
    stats_percent.configure(text = f" {int(round((current_stats[6] / 72), 2) * 100)}%")

def roll_stats_mdsix():
    current_stats = mdsix_set()
    stats_rolls_one.configure(text = f"{current_stats[0][1:]}")
    stats_sum_one.configure(text = f"{current_stats[0][0]}")
    stats_rolls_two.configure(text = f"{current_stats[1][1:]}")
    stats_sum_two.configure(text = f"{current_stats[1][0]}")
    stats_rolls_three.configure(text = f"{current_stats[2][1:]}")
    stats_sum_three.configure(text = f"{current_stats[2][0]}")
    stats_rolls_four.configure(text = f"{current_stats[3][1:]}")
    stats_sum_four.configure(text = f"{current_stats[3][0]}")
    stats_rolls_five.configure(text = f"{current_stats[4][1:]}")
    stats_sum_five.configure(text = f"{current_stats[4][0]}")
    stats_rolls_six.configure(text = f"{current_stats[5][1:]}")
    stats_sum_six.configure(text = f"{current_stats[5][0]}")
    stats_total.configure(text = f" {current_stats[6]}")
    stats_percent.configure(text = f" {int(round((current_stats[6] / 72), 2) * 100)}%")

def roll_method_change(event):
    selection = stats_gen_selector.get()
    match selection.strip():
        case "Standard":
            roll_stats_button.configure(command = roll_stats_standard)
        case "3d6":
            roll_stats_button.configure(command = roll_stats_tdsix)
        case "4d6":
            roll_stats_button.configure(command = roll_stats_fdsix)
        case "Mix d6":
            roll_stats_button.configure(command = roll_stats_mdsix)

#main window organization
main = tk.Tk()
main.title("D&D Character Randomizer")
main.geometry('900x500') #425 with 14 columns

#geometry control
main.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight = 1, uniform = "a")
main.rowconfigure(15, weight = 2, uniform = "a")
main.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight = 1, uniform = "a")

#background
#background = PhotoImage(file = "wooden-floor-background.png")
#background_label = ttk.Label(main, image = background, anchor = "nw")
#background_label.grid(row = 0, column = 0, rowspan = 14, columnspan = 12)
main.configure(bg = "navajo white")

#widget creation
class_randomized = ttk.Label(main, text = "cr", anchor = "center")
class_label = ttk.Label(main, text = "Class", anchor = "center")
class_random_selection = Listbox(main, selectmode = tk.MULTIPLE)
class_random_selection.insert(0, "2024 PHB")
class_random_selection.insert(1, "Eberron")

subclass_randomized = ttk.Label(main, text = "sr", anchor = "center")
subclass_label = ttk.Label(main, text = "Subclass", anchor = "center")
#subclass_random_selection = Listbox(main, selectmode = tk.MULTIPLE)

species_randomized = ttk.Label(main, text = "spr", anchor = "center")
species_label = ttk.Label(main, text = "Species", anchor = "center")
species_random_selection = Listbox(main, selectmode = tk.MULTIPLE)
species_random_selection.insert(0, "2024 PHB")
species_random_selection.insert(1, "Eberron")
species_random_selection.insert(2, "Mythozoology")

background_randomized = ttk.Label(main, text = "bgr", anchor = "center")
background_label = ttk.Label(main, text = "Background", anchor = "center")
background_random_selection = Listbox(main, selectmode = tk.MULTIPLE)
background_random_selection.insert(0, "2024 PHB")
background_random_selection.insert(1, "Eberron")

stats_gen_label = ttk.Label(main, text = "Stat Gen Selection", anchor = "center")
stats_gen_selector = ttk.Combobox(main, values = ["Standard", "3d6", "4d6", "Mix d6"], state = "readonly", justify = "left")
stats_gen_selector.set("Standard")

stats_dice_rolls = ttk.Label(main, text = "Dice Rolls", anchor = "e")
stats_to_assign = ttk.Label(main, text = "Stats", anchor = "e")

stats_rolls_one = ttk.Label(main, text = "", anchor = "center")
stats_sum_one = ttk.Label(main, text = "", anchor = "center")

stats_rolls_two = ttk.Label(main, text = "", anchor = "center")
stats_sum_two = ttk.Label(main, text = "", anchor = "center")

stats_rolls_three = ttk.Label(main, text = "", anchor = "center")
stats_sum_three = ttk.Label(main, text = "", anchor = "center")

stats_rolls_four = ttk.Label(main, text = "", anchor = "center")
stats_sum_four = ttk.Label(main, text = "", anchor = "center")

stats_rolls_five = ttk.Label(main, text = "", anchor = "center")
stats_sum_five = ttk.Label(main, text = "", anchor = "center")

stats_rolls_six = ttk.Label(main, text = "", anchor = "center")
stats_sum_six = ttk.Label(main, text = "", anchor = "center")

stats_total = ttk.Label(main, text = "", anchor = "w")
stats_total_label = ttk.Label(main, text = "Total", anchor = "e")

stats_percent = ttk.Label(main, text = "%", anchor = "center")
stats_percent_label = ttk.Label(main, text = "of standard set", anchor = "w")

str_label = ttk.Label(main, text = "Str", anchor = "center")
str_stat = ttk.Entry(main, justify = "right")
str_modifier = ttk.Label(main, text = "+0")

dex_label = ttk.Label(main, text = "Dex", anchor = "center")
dex_stat = ttk.Entry(main, justify = "right")
dex_modifier = ttk.Label(main, text = "+0")

con_label = ttk.Label(main, text = "Con", anchor = "center")
con_stat = ttk.Entry(main, justify = "right")
con_modifier = ttk.Label(main, text = "+0")

int_label = ttk.Label(main, text = "Int", anchor = "center")
int_stat = ttk.Entry(main, justify = "right")
int_modifier = ttk.Label(main, text = "+0")

wis_label = ttk.Label(main, text = "Wis", anchor = "center")
wis_stat = ttk.Entry(main, justify = "right")
wis_modifier = ttk.Label(main, text = "+0")

cha_label = ttk.Label(main, text = "Cha", anchor = "center")
cha_stat = ttk.Entry(main, justify = "right")
cha_modifier = ttk.Label(main, text = "+0")

image_placeholder = ttk.Label(main, text = "Replace with Character Pixel Art", background = "black")

randomize_button = ttk.Button(main, text = "Randomize", command = update_all)
reset_button = ttk.Button(main, text = "Reset Options")
roll_stats_button = ttk.Button(main, text = "Roll Stats", command = roll_stats_standard)

#widget placement

class_randomized.grid(row = 0, column = 0, columnspan = 3, sticky = "nwe")
class_label.grid(row = 1, column = 0, columnspan = 3, sticky = "nwe")
class_random_selection.grid(row = 15, column = 0, columnspan = 3, sticky = "nwe")

subclass_randomized.grid(row = 0, column = 3, columnspan = 3, sticky = "nwe")
subclass_label.grid(row = 1, column = 3, columnspan = 3, sticky = "nwe")
#subclass_random_selection.grid(row = 2, column = 3, columnspan=3, sticky = "nwe")

species_randomized.grid(row = 0, column = 6, columnspan = 3, sticky = "nwe")
species_label.grid(row = 1, column = 6, columnspan = 3, sticky = "nwe")
species_random_selection.grid(row = 15, column = 6, columnspan = 3, sticky = "nwe")

background_randomized.grid(row = 0, column = 9, columnspan = 3, sticky = "nwe")
background_label.grid(row = 1, column = 9, columnspan = 3, sticky = "nwe")
background_random_selection.grid(row = 15, column = 9, columnspan = 3, sticky = "nwe")

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

stats_gen_label.grid(row = 10, column = 0, columnspan = 2, sticky = "nswe")
stats_gen_selector.grid(row = 10, column = 2, columnspan = 2, sticky = "nswe")

stats_dice_rolls.grid(row = 11, column = 0, sticky = "nsew")
stats_to_assign.grid(row = 12, column = 0, sticky = "nswe")

stats_rolls_one.grid(row  = 11, column = 1, sticky = "nswe")
stats_sum_one.grid(row = 12, column = 1, sticky = "nswe")

stats_rolls_two.grid(row = 11, column = 2, sticky = "nswe")
stats_sum_two.grid(row = 12, column = 2, sticky = "nswe")

stats_rolls_three.grid(row = 11, column = 3, sticky = "nswe")
stats_sum_three.grid(row = 12, column = 3, sticky = "nswe")

stats_rolls_four.grid(row = 11, column = 4, sticky = "nswe")
stats_sum_four.grid(row = 12, column = 4, sticky = "nswe")

stats_rolls_five.grid(row = 11, column = 5, sticky = "nswe")
stats_sum_five.grid(row = 12, column = 5, sticky = "nswe")

stats_rolls_six.grid(row = 11, column = 6, sticky = "nswe")
stats_sum_six.grid(row = 12, column = 6, sticky = "nswe")

stats_total_label.grid(row = 13, column = 0, sticky = "nswe")
stats_total.grid(row = 13, column = 1, sticky = "nswe")

stats_percent_label.grid(row = 14, column = 1, columnspan = 2, sticky = "nswe")
stats_percent.grid(row = 14, column = 0, sticky = "nswe")

randomize_button.grid(row = 10, column = 10,  columnspan = 2, sticky = "nwe")
roll_stats_button.grid(row = 10, column = 8,  columnspan = 2, sticky = "nwe")
reset_button.grid(row = 13, column = 10,  columnspan = 2, sticky = "nwe")

image_placeholder.grid(row = 4, column =6 , rowspan = 6, columnspan = 6, sticky = "nsew")

#binds
stats_gen_selector.bind("<<ComboboxSelected>>", roll_method_change)

main.mainloop()