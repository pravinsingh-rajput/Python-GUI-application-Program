#Windows Action Application 
#importing os module
#importing everything from tkinter

import os
from tkinter import *
root = Tk()
root.title("Windows Action")
icon = PhotoImage(file = 'icon.png')
root.iconphoto(False, icon)
root.geometry ("300x300")


def click1(Shutdown):
    os.system("shutdown /s /t 0 ")
def click2(Restart):
    os.system("shutdown  /r /t 0 ")
def click3(Logoff):
    os.system("shutdown -l ")
def click4(Forceshutdown):
    os.system("shutdown /s /f /t 0 ")

l1 = Label(root)
l2 = Label(root)
label1 = Label (root,text = "Press the Following Buttons To Perform action")

#creating Buttons

button1 = Button(root, text = "Shutdown",padx = 38 , pady = 10 , command = lambda: click1("Shutdown"))
button2 = Button(root, text = "Restart",padx = 47 , pady = 10 , command = lambda: click2("Restart"))
button3 = Button(root, text = "Logoff",padx = 47 , pady = 10 , command = lambda: click3("Logoff"))
button4 = Button(root, text = "Forcefully Shutdown",padx = 10 , pady = 10 , command = lambda: click4("Forcefully Shutdown"))

#using pack method to pack and place it on root window

l1.pack()
label1.pack()
l2.pack()

button1.pack()
button2.pack()
button3.pack()
button4.pack()




root.mainloop()
