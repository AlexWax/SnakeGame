import datetime
from tkinter import *
from time import *


class Click:
    def __init__(self):
        self.width = 1536-970
        self.R_max = 96
        self.speed_change = 3
        self.speed_change_2 = 3
        self.delay_new_circle = 10

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
        self.counter_2 = 0
        self.R_1 = 0
        self.R_2 = 0
        self.crl_outline_width_1 = 10
        self.crl_outline_width_2 = 10
        self.main_canvas.delete('circle')

        def rec():
            print({1: datetime.datetime.now()})
            if self.R_1 < 96:
                self.R_1 += 1
                self.counter_1 += 1
                self.crl_outline_width_1 -= 0.1
                self.main_canvas.delete('circle_rad')
                circle_2 = self.main_canvas.create_oval(x - self.R_1, y - self.R_1, x + self.R_1, y + self.R_1,
                                                        fill='', width=self.crl_outline_width_1,
                                                        outline='blue', tags='circle_rad', )
                self.window.after(self.speed_change, rec_2)

        def rec_2():
            print({2: datetime.datetime.now()})
            if self.R_2 < 96:
                self.R_2 += 1
                self.counter_2 += 1
                self.crl_outline_width_2 -= 0.1
                self.main_canvas.delete('circle_rad_2')
                circle_2 = self.main_canvas.create_oval(x - self.R_2, y - self.R_2, x + self.R_2, y + self.R_2,
                                                        fill='', width=self.crl_outline_width_2,
                                                        outline='green', tags='circle_rad_2', )
                self.window.after(self.speed_change_2, rec)


        rec()
        self.window.after(100)


    def binds(self):
        self.main_canvas.bind('<Button-1>', self.water_click)

    def start(self):
        self.window.mainloop()


Click()