from tkinter import *
from tkinter import ttk
from tkinter import font

import time
import datetime

global endTime

def quit(*args):
    root.destroy()

def cant_wait():
    timeLeft = endTime - datetime.datetime.now()
    time = timeLeft - datetime.timedelta(microseconds=timeLeft.microsecond)

    txt.set(timeLeft)

    root.after(1000.cant_wait)

root = Tk()
root.attributes("-fullscreen", False)
root.configure(background="black")
root.bind("x",quit)
root.after(1000,cant_wait)