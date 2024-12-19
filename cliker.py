from tkinter import *


class Click:
    def __init__(self):
        self.width = 1536-970
        self.R_1 = 50
        self.speed_change = 3

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
        self.main_canvas.delete('circle')
        circle = self.main_canvas.create_oval(x-self.R_1, y-self.R_1, x+self.R_1, y+self.R_1,
                                              fill='grey', outline='', tags='circle',)

        self.counter = 0
        self.R_1 = 0

        def rec():
            if self.counter < 96:
                self.counter += 1
                self.main_canvas.itemconfig(circle, fill='grey'+str(self.counter))
                self.window.after(self.speed_change, rec)

        def rec_2():
            if self.R_1 < 50:
                self.R_1 += 1
                self.main_canvas.delete('circle')
                circle_2 = self.main_canvas.create_oval(x - self.R_1, y - self.R_1, x + self.R_1, y + self.R_1,
                                                        fill='', outline='black', tags='circle', )
                self.window.after(self.speed_change, rec_2)

        rec()
        rec_2()

    def binds(self):
        self.main_canvas.bind('<Button-1>', self.water_click)

    def start(self):
        self.window.mainloop()


Click()