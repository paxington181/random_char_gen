import random
import tkinter as tk
from tkinter import ttk



main = tk.Tk()
main.title("D&D Character Randomizer")
main.configure(background="#5d4340")
main.minsize(300, 300)
main.maxsize(500, 500)
main.geometry("400x400+100+100")

ttk.Label(main, text = 'UIs are a headache').pack()


main.mainloop()