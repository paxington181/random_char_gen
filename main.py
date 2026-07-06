import math
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from stat_rolling import tdsix_set, fdsix_set, mdsix_set, mdsix_set_shuffle, hc_tdsix_set, hc_fdsix_set, hc_mdsix_set
from cssb import *

background_color = "gray27"
foreground_color = "gray69"
selected_classes = base_classes + eberron_classes
selected_species = base_species + eberron_species + ravenloft_species + mythozoology_species
selected_backgrounds = base_background + eberron_background + ravenloft_background

def modifier_update(current_stat):
    current_stat = int(current_stat)
    mod = int( math.floor((current_stat - 10) / 2))
    if mod >= 0:
        return f"+{mod}"
    return f"{mod}"

def update_all():
    class_randomized.configure(text = f"{class_roll(selected_classes)}")
    rspec = species_roll(selected_species)
    species_randomized.configure(text = f"{rspec}")
    rback = background_roll(selected_backgrounds)
    background_randomized.configure(text = f"{rback}")

def stats_update(current_stats):
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
    stats_update(current_stats)

def roll_stats_fdsix():
    current_stats = fdsix_set()
    stats_update(current_stats)

def roll_stats_mdsix():
    current_stats = mdsix_set()
    stats_update(current_stats)

def roll_stats_mdsix_shuffle():
    current_stats = mdsix_set_shuffle()
    stats_update(current_stats)

def roll_stats_hc_tdsix():
    current_stats = hc_tdsix_set()
    stats_update(current_stats)

def roll_stats_hc_fdsix():
    current_stats = hc_fdsix_set()
    stats_update(current_stats)

def roll_stats_hc_mdsix():
    current_stats = hc_mdsix_set()
    stats_update(current_stats)

def roll_method_change(event):
    selection = stats_gen_selector.get()
    match selection.strip():
        case "Standard":
            roll_stats_button.configure(command = roll_stats_standard)
        case "3d6":
            roll_stats_button.configure(command = roll_stats_tdsix)
        case "4d6":
            roll_stats_button.configure(command = roll_stats_fdsix)
        case "3 3d6 3 4d6":
            roll_stats_button.configure(command = roll_stats_mdsix)
        case "Mix d6 Shuffle":
            roll_stats_button.configure(command = roll_stats_mdsix_shuffle)
        case "Hardcore 3d6":
            roll_stats_button.configure(command = roll_stats_hc_tdsix)
        case "Hardcore 4d6":
            roll_stats_button.configure(command = roll_stats_hc_fdsix)
        case "Hardcore Mix":
            roll_stats_button.configure(command = roll_stats_hc_mdsix) 

#main window organization
main = tk.Tk()
main.title("D&D Character Randomizer")
main.geometry('900x500') #425 with 14 columns
main.configure(bg = background_color)

#geometry control
main.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight = 1, uniform = "a")
main.rowconfigure(15, weight = 2, uniform = "a")
main.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight = 1, uniform = "a")

#widget creation
class_randomized = ttk.Label(main, text = "cr", anchor = "center", background = background_color, foreground = foreground_color)
class_label = ttk.Label(main, text = "Class", anchor = "center", background = background_color, foreground = foreground_color)

species_randomized = ttk.Label(main, text = "spr", anchor = "center", background = background_color, foreground = foreground_color)
species_label = ttk.Label(main, text = "Species", anchor = "center", background = background_color, foreground = foreground_color)

background_randomized = ttk.Label(main, text = "bgr", anchor = "center", background = background_color, foreground = foreground_color)
background_label = ttk.Label(main, text = "Background", anchor = "center", background = background_color, foreground = foreground_color)

stats_gen_label = ttk.Label(main, text = "Stat Gen Selection", anchor = "center", background = background_color, foreground = foreground_color)
stats_gen_selector = ttk.Combobox(main, values = ["Standard", "3d6", "4d6", "3 3d6 3 4d6", "Mix d6 Shuffle", "Hardcore 3d6", "Hardcore 4d6", "Hardcore Mix"], state = "readonly", justify = "left", background = background_color, foreground = background_color)
stats_gen_selector.set("Standard")

stats_dice_rolls = ttk.Label(main, text = "Dice Rolls", anchor = "e", background = background_color, foreground = foreground_color)
stats_to_assign = ttk.Label(main, text = "Stats", anchor = "e", background = background_color, foreground = foreground_color)

stats_rolls_one = ttk.Label(main, text = "[1, 1, 1]", anchor = "center", background = background_color, foreground = foreground_color)
stats_sum_one = ttk.Label(main, text = "3", anchor = "center", background = background_color, foreground = foreground_color)

stats_rolls_two = ttk.Label(main, text = "[1, 1, 1]", anchor = "center", background = background_color, foreground = foreground_color)
stats_sum_two = ttk.Label(main, text = "3", anchor = "center", background = background_color, foreground = foreground_color)

stats_rolls_three = ttk.Label(main, text = "[1, 1, 1]", anchor = "center", background = background_color, foreground = foreground_color)
stats_sum_three = ttk.Label(main, text = "3", anchor = "center", background = background_color, foreground = foreground_color)

stats_rolls_four = ttk.Label(main, text = "[1, 1, 1]", anchor = "center", background = background_color, foreground = foreground_color)
stats_sum_four = ttk.Label(main, text = "3", anchor = "center", background = background_color, foreground = foreground_color)

stats_rolls_five = ttk.Label(main, text = "[1, 1, 1]", anchor = "center", background = background_color, foreground = foreground_color)
stats_sum_five = ttk.Label(main, text = "3", anchor = "center", background = background_color, foreground = foreground_color)

stats_rolls_six = ttk.Label(main, text = "[1, 1, 1]", anchor = "center", background = background_color, foreground = foreground_color)
stats_sum_six = ttk.Label(main, text = "3", anchor = "center", background = background_color, foreground = foreground_color)

stats_total = ttk.Label(main, text = "", anchor = "w", background = background_color, foreground = foreground_color)
stats_total_label = ttk.Label(main, text = "Total", anchor = "e", background = background_color, foreground = foreground_color)

stats_percent = ttk.Label(main, text = "%", anchor = "center", background = background_color, foreground = foreground_color)
stats_percent_label = ttk.Label(main, text = "of standard set", anchor = "w", background = background_color, foreground = foreground_color)

str_label = ttk.Label(main, text = "Str", anchor = "e", background = background_color, foreground = foreground_color)
str_stat = ttk.Label(main, text = 10, anchor = "center", background = background_color, foreground = foreground_color)
str_modifier = ttk.Label(main, text = "+0", background = background_color, foreground = foreground_color)

dex_label = ttk.Label(main, text = "Dex", anchor = "e", background = background_color, foreground = foreground_color)
dex_stat = ttk.Label(main, text = 10, anchor = "center", background = background_color, foreground = foreground_color)
dex_modifier = ttk.Label(main, text = "+0", background = background_color, foreground = foreground_color)

con_label = ttk.Label(main, text = "Con", anchor = "e", background = background_color, foreground = foreground_color)
con_stat = ttk.Label(main, text = 10, anchor = "center", background = background_color, foreground = foreground_color)
con_modifier = ttk.Label(main, text = "+0", background = background_color, foreground = foreground_color)

int_label = ttk.Label(main, text = "Int", anchor = "e", background = background_color, foreground = foreground_color)
int_stat = ttk.Label(main, text = 10, anchor = "center", background = background_color, foreground = foreground_color)
int_modifier = ttk.Label(main, text = "+0", background = background_color, foreground = foreground_color)

wis_label = ttk.Label(main, text = "Wis", anchor = "e", background = background_color, foreground = foreground_color)
wis_stat = ttk.Label(main, text = 10, anchor = "center", background = background_color, foreground = foreground_color)
wis_modifier = ttk.Label(main, text = "+0", background = background_color, foreground = foreground_color)

cha_label = ttk.Label(main, text = "Cha", anchor = "e", background = background_color, foreground = foreground_color)
cha_stat = ttk.Label(main, text = 10, anchor = "center", background = background_color, foreground = foreground_color)
cha_modifier = ttk.Label(main, text = "+0", background = background_color, foreground = foreground_color)

stat_reset = tk.Button(main, text = "Reset Stats", command = None)
randomize_button = ttk.Button(main, text = "Randomize", command = update_all)
roll_stats_button = ttk.Button(main, text = "Roll Stats", command = roll_stats_standard)

#widget placement

class_randomized.grid(row = 0, column = 0, columnspan = 3, sticky = "nwe")
class_label.grid(row = 1, column = 0, columnspan = 3, sticky = "nwe")

species_randomized.grid(row = 0, column = 6, columnspan = 3, sticky = "nwe")
species_label.grid(row = 1, column = 6, columnspan = 3, sticky = "nwe")

background_randomized.grid(row = 0, column = 9, columnspan = 3, sticky = "nwe")
background_label.grid(row = 1, column = 9, columnspan = 3, sticky = "nwe")

str_label.grid(row = 2, column = 0, sticky = "nwe")
str_stat.grid(row = 2, column = 1, sticky = "nwe")
str_modifier.grid(row = 2, column = 2, sticky = "nwe")

dex_label.grid(row = 3, column = 0, sticky = "nwe")
dex_stat.grid(row = 3, column = 1, sticky = "nwe")
dex_modifier.grid(row = 3, column = 2, sticky = "nwe")

con_label.grid(row = 4, column = 0, sticky = "nwe")
con_stat.grid(row = 4, column = 1, sticky = "nwe")
con_modifier.grid(row = 4, column = 2, sticky = "nwe")

int_label.grid(row = 5, column = 0, sticky = "nwe")
int_stat.grid(row = 5, column = 1, sticky = "nwe")
int_modifier.grid(row = 5, column = 2, sticky = "nwe")

wis_label.grid(row = 6, column = 0, sticky = "nwe")
wis_stat.grid(row = 6, column = 1, sticky = "nwe")
wis_modifier.grid(row = 6, column = 2, sticky = "nwe")

cha_label.grid(row = 7, column = 0, sticky = "nwe")
cha_stat.grid(row = 7, column = 1, sticky = "nwe")
cha_modifier.grid(row = 7, column = 2, sticky = "nwe")

stats_gen_label.grid(row = 9, column = 0, columnspan = 2, sticky = "nswe")
stats_gen_selector.grid(row = 9, column = 2, columnspan = 2, sticky = "nswe")

stats_dice_rolls.grid(row = 10, column = 0, sticky = "nsew")
stats_to_assign.grid(row = 11, column = 0, sticky = "nswe")

stats_rolls_one.grid(row  = 10, column = 1, sticky = "nswe")
stats_sum_one.grid(row = 11, column = 1, sticky = "nswe")

stats_rolls_two.grid(row = 10, column = 2, sticky = "nswe")
stats_sum_two.grid(row = 11, column = 2, sticky = "nswe")

stats_rolls_three.grid(row = 10, column = 3, sticky = "nswe")
stats_sum_three.grid(row = 11, column = 3, sticky = "nswe")

stats_rolls_four.grid(row = 10, column = 4, sticky = "nswe")
stats_sum_four.grid(row = 11, column = 4, sticky = "nswe")

stats_rolls_five.grid(row = 10, column = 5, sticky = "nswe")
stats_sum_five.grid(row = 11, column = 5, sticky = "nswe")

stats_rolls_six.grid(row = 10, column = 6, sticky = "nswe")
stats_sum_six.grid(row = 11, column = 6, sticky = "nswe")

stats_total_label.grid(row = 12, column = 0, sticky = "nswe")
stats_total.grid(row = 12, column = 1, sticky = "nswe")

stats_percent_label.grid(row = 13, column = 1, columnspan = 2, sticky = "nswe")
stats_percent.grid(row = 13, column = 0, sticky = "nswe")

randomize_button.grid(row = 9, column = 10,  columnspan = 2, sticky = "nwe")
roll_stats_button.grid(row = 9, column = 8,  columnspan = 2, sticky = "nwe")
stat_reset.grid(row = 11, column = 8, columnspan = 2, sticky = "nwe")

#binds
stats_gen_selector.bind("<<ComboboxSelected>>", roll_method_change)

main.mainloop()