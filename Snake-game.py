from tkinter import *
from time import *
from random import *


class Snake:
    def __init__(self):
        self.width = 500
        self.height = 400
        self.R = 5
        self.R_food = 2

        self.news = ['up', 'dn', 'lf', 'rt']
        self.step = 0
        self.speed = 2
        self.stop_motion = 100
        self.tail_crl = []
        self.tail_pos = []
        self.cfs = {}

        self.main()
        self.binds()
        self.vars()
        self.traces()
        self.start()

    def up(self, *args):
        self.text.set('up')
        self.bol.set(True)

    def down(self, *args):
        self.text.set('dn')

    def left(self, *args):
        self.text.set('lt')

    def right(self, *args):
        self.text.set('rt')

    def motion(self, *args):

        self.check()
        self.coords.set(self.cnv.coords(self.crl))
        self.coords_tail.set(str(self.cfs).strip('{}'))

        if self.key:
            self.text.trace_vdelete('w', self.a)
            self.key = False

        [lbl.configure(bg='grey96') for lbl in self.lbls]

        if self.bol.get():
            self.cf = [0 for i in range(2)]
            for tail in self.tail_crl:
                self.cfs[tail] = self.cnv.coords(tail)
            if self.text.get() == 'lt':
                self.cf[0] = 1
                self.lbls[2].configure(bg='grey')
                self.cnv.move(self.crl, -self.speed, 0)
                self.wdw.after(self.stop_motion, self.motion)
            if self.text.get() == 'rt':
                self.cf[0] = -1
                self.lbls[3].configure(bg='grey')
                self.cnv.move(self.crl, self.speed, 0)
                self.wdw.after(self.stop_motion, self.motion)
            if self.text.get() == 'up':
                self.cf[1] = 1
                self.lbls[0].configure(bg='grey')
                self.cnv.move(self.crl, 0, -self.speed)
                self.wdw.after(self.stop_motion, self.motion)
            if self.text.get() == 'dn':
                self.cf[1] = -1
                self.lbls[1].configure(bg='grey')
                self.cnv.move(self.crl, 0, self.speed)
                self.wdw.after(self.stop_motion, self.motion)
            self.mov_to()


    def mov_to(self):
        for tail in self.tail_crl[1:]:
            x = (self.cfs[tail-1][0] + self.cfs[tail-1][2])/2 + self.R*self.cf[0] - self.R - 1
            y = (self.cfs[tail-1][1] + self.cfs[tail-1][3])/2 + self.R*self.cf[1] - self.R - 1
            self.cnv.moveto(tail, x, y)

    def ext(self, *args):
        self.tail_pos.append([self.coords.get()[0] + self.R*self.cf[0], self.coords.get()[1] + self.R*self.cf[1],
                              self.coords.get()[2] + self.R*self.cf[0], self.coords.get()[3] + self.R*self.cf[1]])

        self.tail_crl.append(self.cnv.create_oval(self.tail_pos[-1], fill='green'))

    def check(self):
        x = (self.cnv.coords(self.crl)[0] + self.cnv.coords(self.crl)[2]) / 2
        y = (self.cnv.coords(self.crl)[1] + self.cnv.coords(self.crl)[3]) / 2
        x_food = (self.cnv.coords(self.cnv_food)[0] + self.cnv.coords(self.cnv_food)[2]) / 2
        y_food = (self.cnv.coords(self.cnv_food)[1] + self.cnv.coords(self.cnv_food)[3]) / 2

        if y < self.R or y > self.height/2-self.R or x < self.R or x > self.width/2-self.R:
            self.start_error()
        for tail in self.tail_crl[1:]:
            ranges = self.cnv.coords(tail)
            if (ranges[0] + self.R / 2 < x < ranges[2] - self.R / 2 and ranges[1]
                    + self.R / 2 < y < ranges[3] - self.R / 2):
                self.start_error()

        if self.cnv.coords(self.crl)[0] <= x_food <= self.cnv.coords(self.crl)[2] and \
            self.cnv.coords(self.crl)[1] <= y_food <= self.cnv.coords(self.crl)[3]:
            self.cnv.moveto(self.cnv_food, randint(self.R, int(self.width / 2) - self.R), randint(self.R, int(self.height / 2) - self.R))
            self.ext()

    def main(self):
        self.wdw = Tk()
        self.wdw.geometry(f"{self.width}x{self.height}")
        self.cnv = Canvas(self.wdw, bd=3)
        self.cnv.place(x=self.width / 8, y=self.height / 8, width=self.width / 2, height=self.height / 2)
        self.cnv.focus_set()
        x_food, y_food = randint(self.R, int(self.width / 2) - self.R), randint(self.R, int(self.height / 2) - self.R)
        self.cnv_food = self.cnv.create_oval(x_food - self.R_food, y_food - self.R_food, x_food + self.R_food,
                                             y_food + self.R_food, fill='grey96')
        self.crl = self.cnv.create_oval(self.width / 4 - self.R, self.height / 4 - self.R, self.width / 4 + self.R, self.height / 4 + self.R, fill='green')
        self.tail_crl.append(self.crl)
        self.frm = Frame(self.wdw, bd=3, relief=GROOVE)
        self.frm.place(x=3*self.width/8-50, y=5*self.height / 8, width=100, height=100)
        self.lbls = [Label(self.frm, text=name) for name in self.news]
        self.lbls[0].place(x=50-10, y=10, width=20, height=20)
        self.lbls[1].place(x=50-10, y=100-30, width=20, height=20)
        self.lbls[2].place(x=10, y=50-10, width=20, height=20)
        self.lbls[3].place(x=100-30, y=50-10, width=20, height=20)
        self.lbl_crd_head = Label(self.wdw, justify='center', bd=3, relief=GROOVE)
        self.lbl_crd_head.place(x=5*self.width/8+25, y=1*self.height / 8, width=self.width / 4, height=3*self.width / 16)
        self.lbl_crd_tail = Label(self.wdw, justify='center', bd=3, relief=GROOVE, wraplength=155)
        self.lbl_crd_tail.place(x=5 * self.width / 8 + 25/2, y=3 * self.height / 8, width=self.width / 3,
                           height=3 * self.width / 16)

    def vars(self):
        self.coords = Variable()
        self.coords_tail = Variable()
        self.text = StringVar()
        self.bol = BooleanVar()
        self.bol.set(True)

        self.lbl_crd_head.configure(textvariable=self.coords)
        self.lbl_crd_tail.configure(textvariable=self.coords_tail)

    def binds(self):
        self.cnv.bind('<Up>', self.up)
        self.cnv.bind('<Down>', self.down)
        self.cnv.bind('<Left>', self.left)
        self.cnv.bind('<Right>', self.right)

    def traces(self):
        self.a = self.text.trace('w', self.motion)
        self.key = True

    def start(self):
        self.wdw.mainloop()

    def again(self):
        self.wdw2.destroy()
        Snake()

    def start_error(self):
        self.wdw.destroy()
        self.wdw2 = Tk()
        self.wdw2.geometry(f"{self.width}x{self.height}")
        Label(self.wdw2, text='You lose!', justify='center').place(x=0, y=0, width=self.width, height=self.height/2)
        Button(self.wdw2, text='Start', command=self.again, relief=GROOVE).place(x=self.width/3-50, y=2*self.height/3, width=100, height=50)
        Button(self.wdw2, text='Exit', command=self.wdw2.destroy, relief=GROOVE).place(x=2*self.width/3-50, y=2*self.height/3, width=100, height=50)
        self.wdw2.mainloop()


Snake()