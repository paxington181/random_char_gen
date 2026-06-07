import random
import tkinter as tk
from tkinter import ttk

def tdsix():
    tds_list = []
    for i in range(0, 3):
        tds_list.append(random.randrange(1, 7))
        i += 1
    tds_sorted = sorted(tds_list)
    tds_flipped = tds_sorted[::-1]
    return tds_flipped

def fdsix():
    fds_list = []
    for i in range(0, 4):
        fds_list.append(random.randrange(1, 7))
        i += 1
    fds_sorted = sorted(fds_list)
    fds_flipped = fds_sorted[::-1]
    return fds_flipped[:3]

def reroll_stats():
    dice_rolls_one = fdsix()
    stats_rolls_one.configure(text = f"{dice_rolls_one}")
    stats_sum_one.configure(text = f"{sum(dice_rolls_one)}")
    dice_rolls_two = fdsix()
    stats_rolls_two.configure(text = f"{dice_rolls_two}")
    stats_sum_two.configure(text = f"{sum(dice_rolls_two)}")
    dice_rolls_three = fdsix()
    stats_rolls_three.configure(text = f"{dice_rolls_three}")
    stats_sum_three.configure(text = f"{sum(dice_rolls_three)}")
    dice_rolls_four = fdsix()
    stats_rolls_four.configure(text = f"{dice_rolls_four}")
    stats_sum_four.configure(text = f"{sum(dice_rolls_four)}")
    dice_rolls_five = fdsix()
    stats_rolls_five.configure(text = f"{dice_rolls_five}")
    stats_sum_five.configure(text = f"{sum(dice_rolls_five)}")
    dice_rolls_six = fdsix()
    stats_rolls_six.configure(text = f"{dice_rolls_six}")
    stats_sum_six.configure(text = f"{sum(dice_rolls_six)}")

dice_rolls_one = fdsix()
dice_rolls_two = fdsix()
dice_rolls_three = fdsix()
dice_rolls_four = fdsix()
dice_rolls_five = fdsix()
dice_rolls_six = fdsix()

#main window organization
main = tk.Tk()
main.title("D&D Character Randomizer")
main.geometry('900x425')

#geometry control

main.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), uniform = "a")
main.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight = 1, uniform = "a")

#widget creation

class_randomized = ttk.Label(main, text = "cr", background = "pink", anchor = "center")
class_label = ttk.Label(main, text = "Class", anchor = "center")
class_random_selection = ttk.Button(main, text = "Class Source Options")

subclass_randomized = ttk.Label(main, text = "sr", background = "blue", anchor = "center")
subclass_label = ttk.Label(main, text = "Subclass", anchor = "center")
subclass_random_selection = ttk.Button(main, text = "Subclass Source Options")

species_randomized = ttk.Label(main, text = "spr", background = "green", anchor = "center")
species_label = ttk.Label(main, text = "Species", anchor = "center")
species_random_selection = ttk.Button(main, text = "Species Source Options")

background_randomized = ttk.Label(main, text = "bgr", background = "red", anchor = "center")
background_label = ttk.Label(main, text = "Background", anchor = "center")
background_random_selection = ttk.Button(main, text = "Background Source Options")

stats_gen_label = ttk.Label(main, text = "Stat Gen Selection", anchor = "center")
stats_gen_selector = ttk.Button(main, text = "Replace with Radio?")

stats_dice_rolls = ttk.Label(main, text = "Dice Rolls", anchor = "center")
stats_to_assign = ttk.Label(main, text = "Stats", anchor = "center")

stats_rolls_one = ttk.Label(main, text = f"{dice_rolls_one}", anchor = "center")
stats_sum_one = ttk.Label(main, text = f"{sum(dice_rolls_one)}", anchor = "center")

stats_rolls_two = ttk.Label(main, text = f"{dice_rolls_two}", anchor = "center")
stats_sum_two = ttk.Label(main, text = f"{sum(dice_rolls_two)}", anchor = "center")

stats_rolls_three = ttk.Label(main, text = f"{dice_rolls_three}", anchor = "center")
stats_sum_three = ttk.Label(main, text = f"{sum(dice_rolls_three)}", anchor = "center")

stats_rolls_four = ttk.Label(main, text = f"{dice_rolls_four}", anchor = "center")
stats_sum_four = ttk.Label(main, text = f"{sum(dice_rolls_four)}", anchor = "center")

stats_rolls_five = ttk.Label(main, text = f"{dice_rolls_five}", anchor = "center")
stats_sum_five = ttk.Label(main, text = f"{sum(dice_rolls_five)}", anchor = "center")

stats_rolls_six = ttk.Label(main, text = f"{dice_rolls_six}", anchor = "center")
stats_sum_six = ttk.Label(main, text = f"{sum(dice_rolls_six)}", anchor = "center")

stats_total = ttk.Label(main, text = "stats_total", anchor = "w")
stats_total_label = ttk.Label(main, text = "Sum of stats", anchor = "e")

stats_percent = ttk.Label(main, text = "stats percent", anchor = "w")
stats_percent_label = ttk.Label(main, text = "Percent of standard", anchor = "e")

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

randomize_button = ttk.Button(main, text = "Randomize")
reset_button = ttk.Button(main, text = "Reset Options")
reroll_stats_button = ttk.Button(main, text = "Reroll Stats", command = reroll_stats)

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

stats_total_label.grid(row = 13, column = 0, columnspan = 2, sticky = "nswe")
stats_total.grid(row = 13, column = 2, sticky = "nswe")

stats_percent_label.grid(row = 14, column = 0, columnspan = 2, sticky = "nswe")
stats_percent.grid(row = 14, column = 2, sticky = "nswe")

randomize_button.grid(row = 10, column = 10,  columnspan = 2, sticky = "nwe")
reroll_stats_button.grid(row = 10, column = 8,  columnspan = 2, sticky = "nwe")
reset_button.grid(row = 14, column = 10,  columnspan = 2, sticky = "nwe")

image_placeholder.grid(row = 4, column =6 , rowspan = 6, columnspan = 6, sticky = "nsew")

main.mainloop()