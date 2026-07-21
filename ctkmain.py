import customtkinter
from stat_rolling import standard, tdsix_set, fdsix_set, mdsix_set, mdsix_set_shuffle, hc_tdsix_set, hc_fdsix_set, hc_mdsix_set, modifier_calc
from species import species_roll
from backgrounds import background_roll
from char_class import class_roll

customtkinter.set_appearance_mode("dark")

#Class/sub, background, species
class char_roll(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.columnconfigure((0, 1, 2, 3), uniform = "a")
        
        self.cha_class_label = customtkinter.CTkLabel(self, text = "Class: ")
        self.cha_class_label.grid(row = 0, column = 0, padx = (15, 5), sticky = "e")
        self.cha_class = customtkinter.CTkLabel(self, text = "Snuffleupagus, friend of Large Bird")
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
        self.class_books.grid(row = 0, rowspan = 4, column = 6, columnspan =2, padx = (15, 5), sticky = "ew")
        self.subclass_books = BooksFrame(self, "SubClass Books", books = ["2024 PHB", "Eberron", "Ravenloft"])
        self.subclass_books.grid(row = 0, rowspan = 4, column = 8, columnspan =2, padx = (5, 5), sticky = "ew")
        self.species_books = BooksFrame(self, "Species Books", books = ["2024 PHB", "Eberron", "Ravenloft"])
        self.species_books.grid(row = 0, rowspan = 4, column = 10, columnspan =2, padx = (5, 5), sticky = "ew")
        self.background_books = BooksFrame(self, "Background Books", books = ["2024 PHB", "Eberron", "Ravenloft"])
        self.background_books.grid(row = 0, rowspan = 4, column = 12, columnspan =2, padx = (5, 5), sticky = "ew")


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

class stat_roll(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.rowconfigure((0, 1, 2, 3, 4, 5), uniform = "y")
        self.str_stat = 3
        self.str_mod = modifier_calc(self.str_stat)
        self.dex_stat = 3
        self.dex_mod = modifier_calc(self.dex_stat)
        self.con_stat = 3
        self.con_mod = modifier_calc(self.con_stat)
        self.int_stat = 3
        self.int_mod = modifier_calc(self.int_stat)
        self.wis_stat = 3
        self.wis_mod = modifier_calc(self.wis_stat)
        self.cha_stat = 3
        self.cha_mod = modifier_calc(self.cha_stat)
        self.roll_values = ["15", "14", "13", "12", "10", "8"]
        self.rolling_method = ["Standard", "3d6", "4d6", "3 3d6, 3 4d6", "Random 3d6/4d6", "Hardcore 3d6", "Hardcore 4d6", "Hardcore Random"]

        self.str_stat_label = customtkinter.CTkLabel(self, text = f"Str: {self.str_stat} {self.str_mod}")
        self.str_stat_label.grid(row = 0, column = 0, padx = 10, sticky = "ew")
        self.str_combobox = customtkinter.CTkComboBox(self, values = self.roll_values, command = lambda val: self.str_update(self.str_combobox.get()))
        self.str_combobox.grid(row = 0, column = 1, padx = (0, 10), sticky = "w")
        self.str_combobox.set(self.roll_values[0])

        self.dex_stat_label = customtkinter.CTkLabel(self, text = f"Dex: {self.dex_stat} {self.dex_mod}")
        self.dex_stat_label.grid(row = 1, column = 0, padx = 10, sticky = "ew")
        self.dex_combobox = customtkinter.CTkComboBox(self, values = self.roll_values, command = lambda val: self.dex_update(self.dex_combobox.get()))
        self.dex_combobox.grid(row = 1, column = 1, padx = (0, 10), sticky = "w")
        self.dex_combobox.set(self.roll_values[1])

        self.con_stat_label = customtkinter.CTkLabel(self, text = f"Con: {self.con_stat} {self.con_mod}")
        self.con_stat_label.grid(row = 2, column = 0, padx = 10, sticky = "ew")
        self.con_combobox = customtkinter.CTkComboBox(self, values = self.roll_values, command = lambda val: self.con_update(self.con_combobox.get()))
        self.con_combobox.grid(row = 2, column = 1, padx = (0, 10), sticky = "w")
        self.con_combobox.set(self.roll_values[2])

        self.int_stat_label = customtkinter.CTkLabel(self, text = f"Int: {self.int_stat} {self.int_mod}")
        self.int_stat_label.grid(row = 3, column = 0, padx = 10, sticky = "ew")
        self.int_combobox = customtkinter.CTkComboBox(self, values = self.roll_values, command = lambda val: self.int_update(self.int_combobox.get()))
        self.int_combobox.grid(row = 3, column = 1, padx = (0, 10), sticky = "w")
        self.int_combobox.set(self.roll_values[3])

        self.wis_stat_label = customtkinter.CTkLabel(self, text = f"Wis: {self.wis_stat} {self.wis_mod}")
        self.wis_stat_label.grid(row = 4, column = 0, padx = 10, sticky = "ew")
        self.wis_combobox = customtkinter.CTkComboBox(self, values = self.roll_values, command = lambda val: self.wis_update(self.wis_combobox.get()))
        self.wis_combobox.grid(row = 4, column = 1, padx = (0, 10), sticky = "w")
        self.wis_combobox.set(self.roll_values[4])

        self.cha_stat_label = customtkinter.CTkLabel(self, text = f"Cha: {self.cha_stat} {self.cha_mod}")
        self.cha_stat_label.grid(row = 5, column = 0, padx = 10, sticky = "ew")
        self.cha_combobox = customtkinter.CTkComboBox(self, values = self.roll_values, command = lambda val: self.cha_update(self.cha_combobox.get()))
        self.cha_combobox.grid(row = 5, column = 1, padx = (0, 10), sticky = "w")
        self.cha_combobox.set(self.roll_values[5])

        self.selected_method = customtkinter.CTkComboBox(self, values = self.rolling_method)
        self.selected_method.grid(row = 5, column = 2, columnspan = 2, sticky = "ew")
        self.selected_method.set("Standard")

        self.roll_stats = customtkinter.CTkButton(self, text = "Randomize Stats")
        self.roll_stats.grid(row =5, column = 4, sticky = "ew")

    def str_update(self, value):
        self.str_stat = int(value)
        self.str_mod = modifier_calc(self.str_stat)
        self.str_stat_label.configure(text = f"Str: {self.str_stat} {self.str_mod}")
    
    def dex_update(self, value):
        self.dex_stat = int(value)
        self.dex_mod = modifier_calc(self.dex_stat)
        self.dex_stat_label.configure(text = f"Dex: {self.dex_stat} {self.dex_mod}")

    def con_update(self, value):
        self.con_stat = int(value)
        self.con_mod = modifier_calc(self.con_stat)
        self.con_stat_label.configure(text = f"Con: {self.con_stat} {self.con_mod}")

    def int_update(self, value):
        self.int_stat = int(value)
        self.int_mod = modifier_calc(self.int_stat)
        self.int_stat_label.configure(text = f"Int: {self.int_stat} {self.int_mod}")

    def wis_update(self, value):
        self.wis_stat = int(value)
        self.wis_mod = modifier_calc(self.wis_stat)
        self.wis_stat_label.configure(text = f"Wis: {self.wis_stat} {self.wis_mod}")

    def cha_update(self, value):
        self.cha_stat = int(value)
        self.cha_mod = modifier_calc(self.cha_stat)
        self.cha_stat_label.configure(text = f"Cha: {self.cha_stat} {self.cha_mod}")

class dice_block(customtkinter.CTkFrame):
    def __init__(self, master, roll):
        super().__init__(master)
        self.roll = roll

        if len(self.roll == 3):
            for i, value in enumerate(self.roll):
                label = customtkinter.CTkLabel(self, text = value)
                label.grid(row = 0, column = i, padx = 5, sticky = "ew")



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("D&D 2024 Random Character Generator")
        self.geometry("950x425")
        self.grid_propagate(False)
        
        
        
        self.char_roll_frame = char_roll(self)
        self.char_roll_frame.pack(fill = "x", padx = 5, pady = 5)
        
        self.stat_frame = stat_roll(self)
        self.stat_frame.pack(fill = "x", padx = 5, pady = 5)

app = App()
app.mainloop()