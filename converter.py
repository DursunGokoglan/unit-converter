from tkinter import *


class Converter:
    def __init__(self, converting_from, converting_to, multiplier, **kwargs):
        self.entry = Entry()
        self.button_c = Button(text=kwargs.get('button', "Calculate"), command=self.convert)
        self.button_s = Button(text=kwargs.get('button', "Switch"), command=self.switch)
        self.input_unit = Label(text=converting_from)
        self.output_unit = Label(text=converting_to)
        self.result_label = Label()
        self.presenter = Label(text=kwargs.get('presenter', "equals"))
        self.multiplier = multiplier

        self.entry.grid(column=1, row=0)
        self.button_c.grid(column=1, row=2)
        self.button_s.grid(column=2, row=2)
        self.input_unit.grid(column=2, row=0)
        self.output_unit.grid(column=2, row=1)
        self.result_label.grid(column=1, row=1)
        self.presenter.grid(column=0, row=1)

    def convert(self):
        self.result_label.config(text=round(float(self.entry.get()) * self.multiplier, 4))

    def switch(self):
        if self.input_unit.grid_info()["row"] == 0:
            self.input_unit.grid(column=2, row=1)
            self.output_unit.grid(column=2, row=0)

        else:
            self.input_unit.grid(column=2, row=0)
            self.output_unit.grid(column=2, row=1)

        self.entry.delete(0, END)
        self.result_label.config(text="")
        self.multiplier = 1 / self.multiplier
