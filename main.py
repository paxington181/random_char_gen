import random
import tkinter as tk
from tkinter import ttk



main = tk.Tk()
main.title("D&D Character Randomizer")
main.configure(background="#5d4340")
main.minsize(300, 300)
main.maxsize(1000, 500)
main.geometry("700x400+100+100")


ttk.Label(main, text = "Races/Species").grid(row = 0, column = 0)
ttk.Label(main, text = "Class").grid(row = 0, column = 1)
ttk.Label(main, text = "Background").grid(row = 0, column = 3)
ttk.Label(main, text = "'SubRaces/Species'").grid(row = 1, column = 0)
ttk.Label(main, text = "'Sub Class'").grid(row = 1, column = 1)

ttk.Label(main, text = "Dice Rolling Method").grid(row = 0, column = 4)

stat_frame = tk.Frame(main).grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

ttk.Label(stat_frame, text = "Strength").grid(row = 2, column = 0)
str_entry:int = tk.IntVar()
str_entry.set(3)
ttk.Entry(stat_frame, textvariable = str_entry).grid(row = 2, column = 1)

ttk.Label(stat_frame, text = "Dexterity").grid(row = 3, column = 0)
dex_entry:int  = tk.IntVar()
dex_entry.set(3)
ttk.Entry(stat_frame, textvariable = dex_entry).grid(row = 3, column = 1)

ttk.Label(stat_frame, text = "Constitution").grid(row = 4, column = 0)
con_entry:int = tk.IntVar()
con_entry.set(3)
ttk.Entry(stat_frame, textvariable = con_entry).grid(row = 4, column = 1)

ttk.Label(stat_frame, text = "Intellegence").grid(row = 5, column = 0)
int_entry:int = tk.IntVar()
int_entry.set(3)
ttk.Entry(stat_frame, textvariable = int_entry).grid(row = 5, column = 1)

ttk.Label(stat_frame, text = "Wisdom").grid(row = 6, column = 0)
wis_entry:int = tk.IntVar()
wis_entry.set(3)
ttk.Entry(stat_frame, textvariable = wis_entry).grid(row = 6, column = 1)

ttk.Label(stat_frame, text = "Charisma").grid(row = 7, column = 0)
cha_entry:int = tk.IntVar()
cha_entry.set(3)
ttk.Entry(stat_frame, textvariable = cha_entry).grid(row = 7, column = 1)

ttk.Label(main, text = "Picture placeholder").grid(row = 2, column = 3)

ttk.Label(main, text = "Randomize").grid(row = 8, column = 4)
ttk.Label(main, text = "Reset").grid(row = 8, column = 5)


main.mainloop()