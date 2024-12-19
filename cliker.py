import datetime
import random
from tkinter import *
from time import *


class Click:
    def __init__(self):
        self.width = 1536-970
        self.speed_change = 2
        self.factor = 0.5

        self.main_window()
        self.binds()
        self.start()

    def main_window(self):
        self.window = Tk()
        self.window.title('Best clicker in the world')

        self.height = self.window.winfo_screenheight()
        self.window.geometry(f"{self.width}x{self.height}+{970}+{0}")

        self.main_canvas = Canvas(self.window, cursor='target', relief=GROOVE, bg='grey96')
        self.main_canvas.place(x=0, y=0, width=self.width, height=self.height)
        self.main_canvas.focus_set()

    def water_click(self, arg):
        x = arg.x
        y = arg.y

        self.counter_1 = 0
        self.R_1 = 10
        self.main_canvas.delete('circle')

        def rec():
            if self.counter_1 < 50:
                self.R_1 += 1
                self.counter_1 += 1
                self.main_canvas.delete('circle_rad')
                [self.main_canvas.create_oval(x - (self.R_1 - 10*i)*self.factor, y - (self.R_1 - 10*i)*self.factor, x + (self.R_1 - 10*i)*self.factor, y + (self.R_1 - 10*i)*self.factor,
                                            fill='', width=random.randint(1, round((i+1)/2)),
                                            outline='blue', tags='circle_rad') for i in range(1, 5) if self.counter_1 > i*5]

                self.window.after(self.speed_change, rec)


        rec()



    def binds(self):
        self.main_canvas.bind('<Button-1>', self.water_click)

    def start(self):
        self.window.mainloop()


Click()