import customtkinter
from PIL import Image

d6_1 = customtkinter.CTkImage(light_image = Image.open("dice_images/d6_1.bmp"), dark_image = Image.open("dice_images/d6_1.bmp"), size = (16, 16))
d6_2 = customtkinter.CTkImage(light_image = Image.open("dice_images/d6_2.bmp"), dark_image = Image.open("dice_images/d6_2.bmp"), size = (16, 16))
d6_3 = customtkinter.CTkImage(light_image = Image.open("dice_images/d6_3.bmp"), dark_image = Image.open("dice_images/d6_3.bmp"), size = (16, 16))
d6_4 = customtkinter.CTkImage(light_image = Image.open("dice_images/d6_4.bmp"), dark_image = Image.open("dice_images/d6_4.bmp"), size = (16, 16))
d6_5 = customtkinter.CTkImage(light_image = Image.open("dice_images/d6_5.bmp"), dark_image = Image.open("dice_images/d6_5.bmp"), size = (16, 16))
d6_6 = customtkinter.CTkImage(light_image = Image.open("dice_images/d6_6.bmp"), dark_image = Image.open("dice_images/d6_6.bmp"), size = (16, 16))
customtkinter.set_appearance_mode("light")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("test")
        self.geometry("500x500")
        self.d6_3 = customtkinter.CTkLabel(self, image = d6_4, text = "")
        self.d6_3.pack()
        
        
                
        

app = App()
app.mainloop()