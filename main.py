from tkinter import *
from converter import Converter

window = Tk()
window.title("Convert")
window.config(padx=10, pady=10)

converter = Converter("Km", "Mile", 0.621371)
converter.convert()

window.mainloop()
