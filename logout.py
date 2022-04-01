import os
from tkinter import *
import time

root = Tk()

root.geometry("301x220")
root.title('Manager Shutdown')

shutdown_bt = PhotoImage(file = "/home/rusito/.config/i3status/logout/shutdown.png")
restart_bt = PhotoImage(file= "/home/rusito/.config/i3status/logout/restart.png")
logout_bt = PhotoImage(file = "/home/rusito/.config/i3status/logout/logout.png")
close_bt = PhotoImage(file = "/home/rusito/.config/i3status/logout/close.png")
background = PhotoImage(file = "/home/rusito/.config/i3status/logout/background.png")

label1 = Label( root, image = background, highlightthickness = 0, bd = 0)
label1.place(x = 0, y = 0)

def shutdown():
    os.system('poweroff')
    root.destroy()

def restart():
    os.system("reboot")
    root.destroy()

def logout():
    myLabel3 = Label(root, text="Logout")
    myLabel3.pack()
    time.sleep(0)
    os.system('i3-msg exit')

def x():
    root.destroy()

myButtonS = Button(root, image=shutdown_bt, command=shutdown, borderwidth=0, bg="#6e34eb", activebackground="#6e34eb", highlightthickness = 0, bd = 0)
myButtonR = Button(root, image=restart_bt, command=restart, borderwidth=0, bg="#6e34eb", activebackground="#6e34eb", highlightthickness = 0, bd = 0)
myButtonL = Button(root, image=logout_bt, command=logout, borderwidth=0, bg="#6e34eb", activebackground="#6e34eb", highlightthickness = 0, bd = 0)
myButtonX = Button(root,image= close_bt, command=x, borderwidth=0, bg="#6e34eb", activebackground="#6e34eb", highlightthickness = 0, bd = 0)

myButtonS.pack(pady=5)
myButtonR.pack(pady=5)
myButtonL.pack(pady=5)
myButtonX.place(x=250,y =10)

myButtonL.config(font=("Courier", 16, "italic"), borderwidth=0)
myButtonS.config(font=("Courier", 16, "italic"))
myButtonR.config(font=("Courier", 16, "italic"))


root.mainloop()