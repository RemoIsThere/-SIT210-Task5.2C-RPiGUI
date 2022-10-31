from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

ledRed = LED(14)
ledBlue = LED(15)
ledGreen = LED(16)

win=Tk()
win.title("LED Task")
myFont = tkinter.font.Font(family = 'Helvetika', size = 12, weight = "bold")

def ledRedToggle():
    if ledRed.is_lit:
        ledRed.off()
        ledButton1["text"] = "Turn Red LED ON"
    else:
        ledRed.on()
        ledButton1["text"] = "Turn Red LED OFF"

def ledBlueToggle():
    if ledBlue.is_lit:
        ledBlue.off()
        ledButton2["text"] = "Turn Blue LED ON"
    else:
        ledBlue.on()
        ledButton2["text"] = "Turn Blue LED OFF"

def ledGreenToggle():
    if ledGreen.is_lit:
        ledGreen.off()
        ledButton3["text"] = "Turn Green LED ON"
    else:
        ledGreen.on()
        ledButton3["text"] = "Turn Green LED OFF"
        
ledButton1 = Button(win, text = 'Turn Red LED ON', font = myFont, command = ledRedToggle)
ledButton1.grid(row=0, column=1)
ledButton2 = Button(win, text = 'Turn Blue LED ON', font = myFont, command = ledBlueToggle)
ledButton2.grid(row=0, column=2)
ledButton3 = Button(win, text = 'Turn Green LED ON', font = myFont, command = ledGreenToggle)
ledButton3.grid(row=0, column=3)
