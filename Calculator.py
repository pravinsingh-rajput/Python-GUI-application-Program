from tkinter import *

root = Tk()
root.title("Calculator")
icon = PhotoImage(file = "icon.png")
root.iconphoto(False,icon)

e = Entry(root,width = "45",borderwidth = 8)
e.grid(row = 0, column = 0, columnspan = 4, padx =10 ,  pady = 5)

def click(number):
    c = e.get()
    e.delete(0, END)
    e.insert(0,str(c) +str(number))

def clear():
    e.delete(0, END)

def add ():
    fn = e.get()
    global f
    global math
    math = "Addition"
    f = int(fn)
    e.delete(0, END)

def equal ():
    sn = e.get()
    e.delete(0, END)
    if math == "Addition" :
         e.insert(0,f + int(sn))

    if math == "Substraction":
         e.insert(0,f - int(sn))

    if math == "Multiplication":
         e.insert(0,f * int(sn))

    if math == "Division":
         e.insert(0,f / int(sn))


def sub():
    fn = e.get()
    global f
    global math
    math = "Substraction"
    f = int(fn)
    e.delete(0, END)

def mul():
    fn = e.get()
    global f
    global math
    math = "Multiplication"
    f = int(fn)
    e.delete(0, END)

def div():
    fn = e.get()
    global f
    global math
    math = "Division"
    f = int(fn)
    e.delete(0, END)

    


button1 = Button(root, text = "1",padx = 30 , pady = 10,command = lambda: click(1))
button2 = Button(root, text = "2",padx = 30 , pady = 10,command = lambda: click(2))
button3 = Button(root, text = "3",padx = 30 , pady = 10,command = lambda: click(3))
button4 = Button(root, text = "4",padx = 30 , pady = 10,command = lambda: click(4))
button5 = Button(root, text = "5",padx = 30 , pady = 10,command = lambda: click(5))
button6 = Button(root, text = "6",padx = 30 , pady = 10,command = lambda: click(6))
button7 = Button(root, text = "7",padx = 30 , pady = 10,command = lambda: click(7))
button8 = Button(root, text = "8",padx = 30 , pady = 10,command = lambda: click(8))
button9 = Button(root, text = "9",padx = 30 , pady = 10,command = lambda: click(9))
button0 = Button(root, text = "0",padx = 30 , pady = 10,command = lambda: click(0))
buttonadd = Button(root, text = "+",padx = 28 , pady = 10,command = add)
buttonsub = Button(root, text = "- ",padx = 28 , pady = 10,command = sub)
buttonmul = Button(root, text = "* ",padx = 28 , pady = 10,command = mul)
buttondiv = Button(root, text = "/ ",padx = 28 , pady = 10,command = div)

buttonequal = Button(root, text = "=",padx = 28 , pady = 10,command = equal )
buttonclear = Button(root, text = "C",padx = 29 , pady = 10,command =clear)




button1.grid(row = 3, column =0 )
button2.grid(row = 3 , column =1 )
button3.grid(row = 3, column = 2)

button4.grid(row = 2, column =0 )
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)

button7.grid(row = 1, column = 0)
button8.grid(row = 1, column = 1)
button9.grid(row = 1, column = 2)

button0.grid(row = 4, column = 1)
buttonclear.grid(row = 4, column = 0)

buttonadd.grid(row = 3, column = 3)
buttonequal.grid(row = 4, column = 3)

buttonsub.grid(row = 4, column = 2)
buttonmul.grid(row = 1, column = 3)
buttondiv.grid(row = 2, column = 3)
root.mainloop()
