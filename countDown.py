from tkinter import *
from tkinter import ttk
from tkinter import font

import time
import datetime

global endTime

def quit(*args):
    root.destroy()

def cant_wait():
    #Get the time remianing until the event
    timeLeft = endTime - datetime.datetime.now()

    #remove the microseconds part
    time = timeLeft - datetime.timedelta(microseconds=timeLeft.microseconds)
    
    #show the time left
    txt.set(timeLeft)

    #Triggers the countdown after 1000ms
    root.after(1000,cant_wait)

#Use tkinter lib for showing the clock
root = Tk()
root.attributes("-fullscreen", False)
root.configure(background="black")
root.bind("x",quit)
root.after(1000,cant_wait)

#   Set the end date and time for the countdown
endTime = datetime.datetime(2021,9,30,0)
fnt = font.Font(family = "Helvetica", size = 90, weight = "bold")

txt = StringVar()
lbl = ttk.Label(root, textvariable = txt, font = fnt, foreground = "white", background ="black")
lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()