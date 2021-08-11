from tkinter import *
import math 


d=""
s=""
b=""
f=0


def input_n(n):
    global s
    global b
    global d
    global f
    if d == "0":
        d = ""
    d = d + str(n)
    l0.configure(text=s)
    l1.configure(text=d)
    f = 0

def doti():
    global s
    global b
    global d
    global f
    if d.count(".") == 0:
        d = d+"."
        l0.configure(text=d)
        l1.configure(text=s)
    
    

def div():
    global d
    global s
    global b
    global f
    if f == 1:
        s = s[:-1]+"÷"
        b = b[:-1]+"/"
    elif d == "":
        b = "0/"
        s = "0÷"
    else:
        s = str(eval(b+d))
        b = s+"/"
        s = s+"÷"
    l0.configure(text=s)
    l1.configure(text=d)
    d = ""
    f=1


def mul():
    global d
    global s
    global b
    global f
    if f== 1:
        s = s[:-1]+"×"
        d = d[:-1]+"*"
    elif d == "":
        b = "0*"
        s = "0×"
    else:
        s=str(eval(b+d))
        b = s+"*"
        s = s+"×"
    l0.configure(text=s)
    l1.configure(text=d)
    d = ""
    f=1


def add():
    global d
    global s
    global b
    global f
    if f == 1:
        s= s[:-1]+"+"
        d = d[:-1]+"+"
    elif d == "":
        b = "0+"
        s = "0+"
    else:
        s=str(eval(b+d))
        s = s+"+"
        b = s+"+"
    l0.configure(text=s)
    l1.configure(text=d)
    d = ""
    f=1
    


def sub():
    global d
    global s
    global b
    global f
    if f == 1:
        s = s[:-1]+"-"
        d = d[:-1]+"-"
    elif d == "":
        b = "0-"
        s = "0−"
    else:
        s = str(eval(b+d))
        s = s+"-"
        b=s+"-"
    l0.configure(text=s)
    l1.configure(text=d)
    d=""
    f=1
    
def equu():
    global s
    global d
    global b
    global f
    try:
        if d == "":
            d = "0"
        if f == 1:
            b = b[:-1]
            d = "+0"
        b = str(eval(b+d))
        d = b
        s = ""
        l0.configure(text=s)
        l1.configure(text=d)
        b = ""
        f = 0
        if d == "0":
            d = ""
        
    except:
        s=""
        d="Error"
        l0.configure(text=s)
        l1.configure(text=d)
        d=""
        s=""
        f=0
    
    

def clear():
    global d
    global s
    global b
    b = ""
    d = ""
    s = ""
    l0.configure(text="")
    l1.configure(text="0")
        

def ps():
    global d
    global s
    global b
    if d=="":
        d=0
    d = str(float(d)*-1)
    l0.configure(text=s)
    l1.configure(text=d)


def per():
    global d
    global s
    global b
    d = str((float(d))/100)
    b = d
    l0.configure(text=s)
    l1.configure(text=d)
    

def bx1(e):
    b1.configure(bg="#394765")
    input_n(1)


def byy1(e):
    b1.configure(bg="#394765")


def bxx1(e):
    b1.configure(bg="#2e3951")


def bx2(e):
    b2.configure(bg="#394765")
    input_n(2)


def byy2(e):
    b2.configure(bg="#394765")


def bxx2(e):
    b2.configure(bg="#2e3951")


def bx3(e):
    b3.configure(bg="#394765")
    input_n(3)

def byy3(e):
    b3.configure(bg="#394765")


def bxx3(e):
    b3.configure(bg="#2e3951")


def bx4(e):
    b4.configure(bg="#394765")
    input_n(4)


def byy4(e):
    b4.configure(bg="#394765")


def bxx4(e):
    b4.configure(bg="#2e3951")


def bx5(e):
    b5.configure(bg="#394765")
    input_n(5)


def byy5(e):
    b5.configure(bg="#394765")


def bxx5(e):
    b5.configure(bg="#2e3951")


def bx6(e):
    b6.configure(bg="#394765")
    input_n(6)


def byy6(e):
    b6.configure(bg="#394765")


def bxx6(e):
    b6.configure(bg="#2e3951")


def bx7(e):
    b7.configure(bg="#394765")
    input_n(7)


def byy7(e):
    b7.configure(bg="#394765")


def bxx7(e):
    b7.configure(bg="#2e3951")


def bx8(e):
    b8.configure(bg="#394765")
    input_n(8)


def byy8(e):
    b8.configure(bg="#394765")


def bxx8(e):
    b8.configure(bg="#2e3951")


def bx9(e):
    b9.configure(bg="#394765")
    input_n(9)


def byy9(e):
    b9.configure(bg="#394765")


def bxx9(e):
    b9.configure(bg="#2e3951")


def bx0(e):
    b0.configure(bg="#394765")
    input_n(0)


def byy0(e):
    b0.configure(bg="#394765")


def bxx0(e):
    b0.configure(bg="#2e3951")


def dx(e):
    bd.configure(bg="#2a344a")
    div()


def byyd(e):
    bd.configure(bg="#394765")


def bxxdx(e):
    bd.configure(bg="#2a344a")


def mx(e):
    bm.configure(bg="#2a334a")
    mul()


def byym(e):
    bm.configure(bg="#394765")


def bxxmx(e):
    bm.configure(bg="#2a334a")


def eqx(e):
    be.configure(bg="#0DB387")
    equu()


def byye(e):
    be.configure(bg="#10CF9C")


def bxxeqx(e):
    be.configure(bg="#0DB387")


def ax(e):
    ba.configure(bg="#2a334a")
    add()


def byya(e):
    ba.configure(bg="#394765")


def bxxax(e):
    ba.configure(bg="#2a334a")


def sbx(e):
    bs.configure(bg="#2a334a")
    sub()


def byys(e):
    bs.configure(bg="#394765")


def bxxsbx(e):
    bs.configure(bg="#2a334a")


def acx(e):
    bAC.configure(bg="#2a334a")
    clear()


def byyAC(e):
    bAC.configure(bg="#394765")


def bcx(e):
    global d
    bAC.configure(bg="#394765")
    d = d[:-1]
    if d == "":
        d = "0"
    l1.configure(text=d)


def xdx(e):
    bx.configure(bg="#2e3951")
    doti()


def byyxdx(e):
    bx.configure(bg="#394765")


def bxxxdx(e):
    bx.configure(bg="#2e3951")


def bxxxx(e):
    bAC.configure(bg="#2a334a")


def bxp(e):
    bp.configure(bg="#2a334a")
    per()


def bxxp(e):
    bp.configure(bg="#2a334a")


def byyp(e):
    bp.configure(bg="#394765")


def bxxsc(e):
    bsc.configure(bg="#2a334a")


def byysc(e):
    bsc.configure(bg="#394765")






w=Tk()
w.configure(bg="#1f1f1f")
w.title("Simple Calculator")

l0 = Label(text="", fg="#9BD0C6", bg="#182030", font=(
    'Arial', 12 ), anchor="e", padx="15", pady="10")
l1 = Label(text="0", fg="#0DB387", bg="#182030", font=(
    'Arial', 30 ), anchor="e", padx="15", pady="10")

bAC = Button(w, text="AC", font=('Arial', 16), pady="15", padx="15", command=clear, bd=0,
             bg="#2A344A", fg="#e56477", activebackground="#e56477", activeforeground="white")
bsc = Button(w, text="±", font=('Arial', 16), pady="15", padx="18", command=ps,
             bd=0, bg="#2A344A", fg="#0DB387", activebackground="#3A4968", activeforeground="white")
bp = Button(w, text="%", font=('Arial', 16), pady="15", padx="18", command=per,
            bd=0, bg="#2A344A", fg="#0DB387", activebackground="#3A4968", activeforeground="white")
bd = Button(w, text="÷", font=('Arial', 16), pady="15", padx="18", command=div,
            bd=0, bg="#2A344A", fg="#0DB387", activebackground="#3A4968", activeforeground="white")
b7 = Button(w, text="7", font=('Arial', 16), pady="15", padx="15", command=lambda: input_n(
    7), bd=0, bg="#2E3951", fg="#93A59D", activebackground="#3A4968", activeforeground="white")
b8 = Button(w, text="8", font=('Arial', 16), pady="15", padx="18", command=lambda: input_n(
    8), bd=0, bg="#2E3951", fg="#93A59D", activebackground="#3A4968", activeforeground="white")
b9 = Button(w, text="9", font=('Arial', 16), pady="15", padx="18", command=lambda: input_n(
    9), bd=0, bg="#2E3951", fg="#93A59D", activebackground="#3A4968", activeforeground="white")
bm = Button(w, text="✕", font=('Arial', 13), pady="15", padx="18", command=mul,
            bd=0, bg="#2A344A", fg="#0DB387", activebackground="#3A4968", activeforeground="white")
b4 = Button(w, text="4", font=('Arial', 16), pady="15", padx="15", command=lambda: input_n(
    4), bd=0, bg="#2E3951", fg="#93A59D", activebackground="#3A4968", activeforeground="white")
b5 = Button(w, text="5", font=('Arial', 16), pady="15", padx="18", command=lambda: input_n(
    5), bd=0, bg="#2E3951", fg="#93A59D", activebackground="#3A4968", activeforeground="white")
b6 = Button(w, text="6", font=('Arial', 16), pady="15", padx="18", command=lambda: input_n(
    6), bd=0, bg="#2E3951", fg="#93A59D", activebackground="#3A4968", activeforeground="white")
bs = Button(w, text="−", font=('Arial', 16), pady="15", padx="18", command=sub,
            bd=0, bg="#2A344A", fg="#0DB387", activebackground="#3A4968", activeforeground="white")
b1 = Button(w, text="1", font=('Arial', 16), pady="15", padx="18", command=lambda: input_n(
    1), bd=0, bg="#2E3951", fg="#93A59D", activebackground="#3A4968", activeforeground="white")
b2 = Button(w, text="2", font=('Arial', 16), pady="15", padx="15", command=lambda: input_n(
    2), bd=0, bg="#2E3951", fg="#93A59D", activebackground="#3A4968", activeforeground="white")
b3 = Button(w, text="3", font=('Arial', 16), pady="15", padx="18", command=lambda: input_n(
    3), bd=0, bg="#2E3951", fg="#93A59D", activebackground="#3A4968", activeforeground="white")
ba = Button(w, text="+", font=('Arial', 16), pady="15", padx="18", command=add,
            bd=0, bg="#2A344A", fg="#0DB387", activebackground="#3A4968", activeforeground="white")
b0 = Button(w, text="0", font=('Arial', 16), pady="15", padx="18", command=lambda: input_n(
    0), bd=0, bg="#2E3951", fg="#93A59D", activebackground="#3A4968", activeforeground="white")
bx = Button(w, text=".", font=('Arial', 16), pady="15", padx="15", command=doti, bd=0, bg="#2E3951", fg="#93A59D", activebackground="#3A4968", activeforeground="white")
be=Button(w, text="=",font=('Cambria',20),pady="10",padx="18",bd=0,bg="#0DB387",fg="#2A344A",activebackground="#3A4968",activeforeground="white",command=equu)



l0.grid(column=0,row=0,columnspan=4,rowspan=2,sticky="news")
l1.grid(column=0,row=3,columnspan=4,sticky="news")
bAC.grid(column=0,row=4,sticky="news")
bsc.grid(column=1,row=4,sticky="news")
bp.grid(column=2,row=4,sticky="news")
bd.grid(column=3,row=4,sticky="news")
b7.grid(column=0,row=5,sticky="news")
b8.grid(column=1,row=5,sticky="news")
b9.grid(column=2,row=5,sticky="news")
bm.grid(column=3,row=5,sticky="news")
b4.grid(column=0,row=6,sticky="news")
b5.grid(column=1,row=6,sticky="news")
b6.grid(column=2,row=6,sticky="news")
bs.grid(column=3,row=6,sticky="news")
b1.grid(column=0,row=7,sticky="news")
b2.grid(column=1,row=7,sticky="news")
b3.grid(column=2,row=7,sticky="news")
ba.grid(column=3,row=7,sticky="news")
b0.grid(column=0,row=8,columnspan=2,sticky="news")
bx.grid(column=2,row=8,sticky="news")
be.grid(column=3,row=8,sticky="news")


w.bind('1', bx1)
w.bind('<KeyRelease-1>', bxx1)
b1.bind('<Leave>', bxx1)
b1.bind('<Enter>', byy1)

w.bind('%', bxp)
w.bind('<KeyRelease-%>', bxxp)
bp.bind('<Enter>', byyp)
bp.bind('<Leave>', bxxp)

w.bind('2', bx2)
w.bind('<KeyRelease-2>', bxx2)
b2.bind('<Leave>', bxx2)
b2.bind('<Enter>', byy2)

w.bind('3', bx3)
w.bind('<KeyRelease-3>', bxx3)
b3.bind('<Leave>', bxx3)
b3.bind('<Enter>', byy3)

bsc.bind('<Enter>', byysc)
bsc.bind('<Leave>', bxxsc)

w.bind('4', bx4)
w.bind('<KeyRelease-4>', bxx4)
b4.bind('<Leave>', bxx4)
b4.bind('<Enter>', byy4)

w.bind('5', bx5)
w.bind('<KeyRelease-5>', bxx5)
b5.bind('<Leave>', bxx5)
b5.bind('<Enter>', byy5)

w.bind('6', bx6)
w.bind('<KeyRelease-6>', bxx6)
b6.bind('<Leave>', bxx6)
b6.bind('<Enter>', byy6)

w.bind('7', bx7)
w.bind('<KeyRelease-7>', bxx7)
b7.bind('<Leave>', bxx7)
b7.bind('<Enter>', byy7)

w.bind('8', bx8)
w.bind('<KeyRelease-8>', bxx8)
b8.bind('<Leave>', bxx8)
b8.bind('<Enter>', byy8)

w.bind('9', bx9)
w.bind('<KeyRelease-9>', bxx9)
b9.bind('<Leave>', bxx9)
b9.bind('<Enter>', byy9)

w.bind('0', bx0)
w.bind('<KeyRelease-0>', bxx0)
b0.bind('<Leave>', bxx0)
b0.bind('<Enter>', byy0)

w.bind('/', dx)
w.bind('<KeyRelease-/>', bxxdx)
bd.bind('<Leave>', bxxdx)
bd.bind('<Enter>', byyd)

w.bind('*', mx)
w.bind('<KeyRelease-*>', bxxmx)
bm.bind('<Leave>', bxxmx)
bm.bind('<Enter>', byym)

w.bind('-', sbx)
w.bind('<KeyRelease-->', bxxsbx)
bs.bind('<Leave>', bxxsbx)
bs.bind('<Enter>', byys)

w.bind('+', ax)
w.bind('<KeyRelease-+>', bxxax)
ba.bind('<Leave>', bxxax)
ba.bind('<Enter>', byya)

w.bind('=', eqx)
w.bind('<KeyRelease-=>', bxxeqx)
be.bind('<Leave>', bxxeqx)
be.bind('<Enter>', byye)

w.bind('.', xdx)
w.bind('<KeyRelease-.>', bxxxdx)
bx.bind('<Leave>', bxxxdx)
bx.bind('<Enter>', byyxdx)

w.bind('<Return>', eqx)
w.bind('<KeyRelease-Return>', bxxeqx)
be.bind('<Leave>', bxxeqx)
be.bind('<Enter>', byye)

w.bind('<BackSpace>', bcx)
w.bind('<KeyRelease-BackSpace>', bxxxx)
w.bind('<Delete>', acx)
w.bind('<KeyRelease-Delete>', bxxxx)
bAC.bind('<Enter>', byyAC)
bAC.bind('<Leave>', bxxxx)


w.grid_rowconfigure(0, weight=1)
w.grid_rowconfigure(1, weight=1)
w.grid_rowconfigure(2, weight=1)
w.grid_rowconfigure(3, weight=1)
w.grid_rowconfigure(4, weight=1)
w.grid_rowconfigure(5, weight=1)
w.grid_rowconfigure(6, weight=1)
w.grid_rowconfigure(7, weight=1)
w.grid_rowconfigure(8, weight=1)
w.grid_columnconfigure(0, weight=1)
w.grid_columnconfigure(1, weight=1)
w.grid_columnconfigure(2, weight=1)
w.grid_columnconfigure(3, weight=1)

w.mainloop()
