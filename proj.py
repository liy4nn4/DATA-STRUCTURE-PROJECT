from tkinter import *
from PIL import Image, ImageTk
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()


class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("380x212")
        self.title("File Compression")

        
        
def main():
    Window().mainloop()

main() 
