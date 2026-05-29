import tkinter as tk
from tkinter import ttk

#main window organization
main = tk.Tk()
main.title("D&D Character Randomizer")
main.geometry('600x400')

#widget creation
class_label = ttk.Label(main, text = "Class")

species_label = ttk.Label(main, text = "Species")

background_label = ttk.Label(main, text = "Background")

#widget placement


main.mainloop()