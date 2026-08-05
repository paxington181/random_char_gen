import customtkinter
from PIL import Image

d6_3 = customtkinter.CTkImage(light_image = Image.open("dice_images/d6_3.bmp"), dark_image = Image.open("dice_images/d6_3.bmp"), size = (16, 16))
customtkinter.set_appearance_mode("light")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("test")
        self.geometry("500x500")
        self.d6_3 = customtkinter.CTkLabel(self, image = d6_3, text = "")
        self.d6_3.pack()
        
        
                
        

app = App()
app.mainloop()