from tkinter import *


class Converter:
    def __init__(self, converting_from, converting_to, multiplier, **kwargs):
        self.entry = Entry()
        self.entry.insert(END, "0")
        self.button = Button(text=kwargs.get('button', "Calculate"), command=self.convert)
        self.input_unit = Label(text=converting_from)
        self.output_unit = Label(text=converting_to)
        self.result_label = Label()
        self.presenter = Label(text=kwargs.get('presenter', "equals"))
        self.multiplier = multiplier

        self.entry.grid(column=1, row=0)
        self.button.grid(column=1, row=2)
        self.input_unit.grid(column=2, row=0)
        self.output_unit.grid(column=2, row=1)
        self.result_label.grid(column=1, row=1)
        self.presenter.grid(column=0, row=1)

    def convert(self):
        self.result_label.config(text=float(self.entry.get()) * self.multiplier)
