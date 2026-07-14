import customtkinter
import math
#from stat_rolling import tdsix_set, fdsix_set, mdsix_set, mdsix_set_shuffle, hc_tdsix_set, hc_fdsix_set, hc_mdsix_set
from cssb import *
from species import species_roll
from backgrounds import background_roll

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

        self.class_books = BooksFrame(self, "Class Books", books = ["2024 PHB", "Eberron"])
        self.class_books.grid(row = 0, rowspan = 4, column = 6, columnspan =2, sticky = "ew")
        self.subclass_books = BooksFrame(self, "SubClass Books", books = ["2024 PHB", "Eberron", "Ravenloft"])
        self.subclass_books.grid(row = 0, rowspan = 4, column = 8, columnspan =2, padx = (10, 10), sticky = "ew")
        self.species_books = BooksFrame(self, "Species Books", books = ["2024 PHB", "Eberron", "Ravenloft"])
        self.species_books.grid(row = 0, rowspan = 4, column = 10, columnspan =2, padx = (10, 10), sticky = "ew")
        self.background_books = BooksFrame(self, "Background Books", books = ["2024 PHB", "Eberron", "Ravenloft"])
        self.background_books.grid(row = 0, rowspan = 4, column = 12, columnspan =2, padx = (10, 10), sticky = "ew")

    def randomize(self):
        class_rand = self.class_books.get()
        subclass_rand = self.subclass_books.get()
        self.cha_class.configure(text = f"{class_roll(class_rand, subclass_rand)}")
        species_rand = self.species_books.get()
        self.cha_species.configure(text = f"{species_roll(species_rand)}")
        background_rand = self.background_books.get()
        self.cha_background.configure(text = f"{background_roll(background_rand)}")

class BooksFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, books):
        super().__init__(master)
        self.title = title
        self.books = books
        self.checkboxes = []

        self.title = customtkinter.CTkLabel(self, text = self.title, fg_color = "gray30", corner_radius = 6)
        self.title.grid(row = 0, column = 0, columnspan = 2, padx = (10, 10), sticky = "nsew")

        for i, books in enumerate(self.books):
            checkbox = customtkinter.CTkCheckBox(self, text = books)
            checkbox.grid(row = i + 1, column = 0, padx = 10, pady = (10, 0), sticky = "w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("D&D 2024 Random Character Generator")
        self.geometry("950x425")
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight = 1)
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), weight = 1)
        
        
        self.char_roll_frame = char_roll(self)
        self.char_roll_frame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "nsew")
        
   

app = App()
app.mainloop()