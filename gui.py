from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

## Hardware
blueLED = LED(17)
greenLED = LED(27)
redLED = LED(22)

## GUI Definitions
win = Tk()
win.title("LED Toggle System")
customFont = tkinter.font.Font(family="Helvetica", size=12, weight="bold")

## Varibles
ledCode = StringVar()


## Event Functions
def ledToggle():
    ledCodeHolder = ledCode.get()
    if(ledCodeHolder == 'R'):
        blueLED.off()
        greenLED.off()
        redLED.on()
    elif(ledCodeHolder == 'G'):
        blueLED.off()
        redLED.off()
        greenLED.on()
    elif(ledCodeHolder == 'B'):
        redLED.off()
        greenLED.off()
        blueLED.on()
    else:
        redLED.off()
        greenLED.off()
        blueLED.off()

def close():
    GPIO.cleanup()
    win.destroy()

## Widgets Area
redButton = Radiobutton(win, text="Red LED", variable=ledCode, value='R', font=customFont, command=ledToggle, bg='red', height=1, width=24)
redButton.grid(row=0, column=1)

greenButton = Radiobutton(win, text="Green LED", variable=ledCode, value='G',  font=customFont, command=ledToggle, bg='green', height=1, width=24)
greenButton.grid(row=3, column=1)

blueButton = Radiobutton(win, text="Blue LED", variable=ledCode, value='B', font=customFont, command=ledToggle, bg="lightblue", height=1, width=24)
blueButton.grid(row=5, column=1)

exitButton = Button(win, text="Exit", font=customFont, command=close, bg="orange", height=1, width=12)
exitButton.grid(row=7, column=1)


## Highlevel events
win.protocol("WM_DELETE_WINDOW", close) #Clean exit using close 'x'
win.mainloop() #Loops forever - needed for larger applications
