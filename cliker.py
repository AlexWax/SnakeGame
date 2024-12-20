import datetime
import random
from tkinter import *
from time import *


class Click:
    def __init__(self):
        self.width = 1536-970


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
        self.speed_change = random.randint(2, 3)
        self.nums_of_ovals = random.randint(4, 6)
        print(self.nums_of_ovals)
        self.counter_1 = 0
        self.R_1 = 10
        self.dist_b_ovals = [random.randint(3, 10) / 10 for i in range(self.nums_of_ovals - 1)]

        def rec():
            if self.counter_1 < 125:
                self.R_1 += 1
                self.counter_1 += 1

                self.main_canvas.delete('circle_rad')
                ovals = [self.main_canvas.create_oval(x-2 - (self.R_1 - 10*i)*self.dist_b_ovals[i-1], y+2 - (self.R_1 - 10*i)*self.dist_b_ovals[i-1],
                                              x + (self.R_1 - 10*i)*self.dist_b_ovals[i-1], y + (self.R_1 - 10*i)*self.dist_b_ovals[i-1],
                                            fill='', width=random.randint(1, round((i+1)/2)),
                                            outline='dodgerblue', tags='circle_rad') for i in range(1, self.nums_of_ovals) if self.counter_1 > i*self.dist_b_ovals[i-1]]
                [self.main_canvas.itemconfig(ovals[i], width=0) for i in range(self.nums_of_ovals-1) if self.R_1 >= 90 + 10*i]

                self.window.after(self.speed_change, rec)

        rec()

    def binds(self):
        self.main_canvas.bind('<Button-1>', self.water_click)

    def start(self):
        self.window.mainloop()


Click()