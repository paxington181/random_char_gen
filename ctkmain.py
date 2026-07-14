import customtkinter
import math
#from stat_rolling import tdsix_set, fdsix_set, mdsix_set, mdsix_set_shuffle, hc_tdsix_set, hc_fdsix_set, hc_mdsix_set
from cssb import *

customtkinter.set_appearance_mode("dark")

#Class/sub, background, species
class char_roll(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.cha_class_label = customtkinter.CTkLabel(self, text = "Class: ")
        self.cha_class_label.grid(row = 0, column = 0, padx = (15, 5), sticky = "e")
        self.cha_class = customtkinter.CTkLabel(self, text = "Snuffleupagus, friend of Big Bird of the Yellow")
        self.cha_class.grid(row = 0, column = 1, columnspan = 4, sticky = "w")
        self.cha_species_label = customtkinter.CTkLabel(self, text = "Species: ")
        self.cha_species_label.grid(row = 1, column = 0, padx = (15, 5), sticky = "e")
        self.cha_species = customtkinter.CTkLabel(self, text = "Imaginary Friend")
        self.cha_species.grid(row = 1, column = 1, columnspan = 3, sticky = "w")
        self.cha_background_label = customtkinter.CTkLabel(self, text = "Background: ")
        self.cha_background_label.grid(row = 2, column = 0, padx = (15, 5), sticky = "e")
        self.cha_background = customtkinter.CTkLabel(self, text = "Dream of the Yellow Bird")
        self.cha_background.grid(row = 2, column = 1, columnspan = 3, sticky = "w")
        self.randomize_button = customtkinter.CTkButton(self, text = "Roll Character", command = self.randomize)
        self.randomize_button.grid(row = 3, column = 0, columnspan = 5, padx = 10, sticky = "ew")

    def randomize(self):
        pass


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("D&D 2024 Random Character Generator")
        self.geometry("900x425")
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight = 1)
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight = 1)
        
        
        self.char_roll_frame = char_roll(self)
        self.char_roll_frame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "nsew")
        
app = App()
app.mainloop()