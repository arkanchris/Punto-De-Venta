from tkinter import *
from tkinter import ttk
import sys
import os 


class Manager (tk):
    def __init (self, *args, **kwagrs):
        super().__init__(*args, **kwagrs )
        self.title("Mini Market v1.0")
        self.geometry("1100x650+120+20")
        self.resizable(False, False)

        container = Frame(self)
        container.pack(side=TOP, fill=BOTH, expand=True)
        container.configure(bg="#C6D9E3")

        self.frame = {}
        for i in (Login, registro, Container):
            frame = i(container, self)
            self.frames[i] = frame


