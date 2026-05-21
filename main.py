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
ttk.Label(main, text = "Strength").grid(row = 2, column = 0)
ttk.Label(main, text = "Strength number").grid(row = 2, column = 1)
ttk.Label(main, text = "Dexterity").grid(row = 3, column = 0)
ttk.Label(main, text = "Dexterity number").grid(row = 3, column = 1)
ttk.Label(main, text = "Constitution").grid(row = 4, column = 0)
ttk.Label(main, text = "Constitution number").grid(row = 4, column = 1)
ttk.Label(main, text = "Intellegence").grid(row = 5, column = 0)
ttk.Label(main, text = "Intellegence number").grid(row = 5, column = 1)
ttk.Label(main, text = "Wisdom").grid(row = 6, column = 0)
ttk.Label(main, text = "Wisdom number").grid(row = 6, column = 1)
ttk.Label(main, text = "Charisma").grid(row = 7, column = 0)
ttk.Label(main, text = "Charisma number").grid(row = 7, column = 1)
ttk.Label(main, text = "Picture placeholder").grid(row = 2, column = 3)
ttk.Label(main, text = "Randomize").grid(row = 8, column = 4)
ttk.Label(main, text = "Reset").grid(row = 8, column = 5)


main.mainloop()