from tkinter import *
from converter import Converter

input_unit = input("Enter input unit: ")
output_unit = input("Enter output unit: ")
ratio = float(input("Enter input/output ratio: "))

window = Tk()
window.title("Convert")
window.config(padx=10, pady=10)

converter = Converter(input_unit, output_unit, ratio)

window.mainloop()
