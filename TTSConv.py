from tkinter import *
from gtts import gTTS
from playsound import playsound
import gi

root = Tk()   #Blanck window
root.title("Text to Speech Converter")
root.geometry("350x300")

label1 = Label(root, text="TEXT_TO_SPEECH_CONVERTER",fg='black')
label1.pack()

label2 = Label(root, text="Enter Text:",fg='black')
label2.place(x=20,y=60)

message = StringVar()
entry = Entry(root, textvariable=message)
entry.place(x=20,y=100)


def text_to_speech():
    msg = entry.get()
    speech = gTTS(text=msg)
    speech.save('DataFlair.mp3')
    playsound("DataFlair.mp3")

def Exit():
    root.destroy()    #or exit() both works

def reset():
    message.set("")

button1 = Button(root, text="PLAY", fg='black', command=text_to_speech)
button2 = Button(root, text="Exit", bg="red", fg='black', command=Exit)
button3 = Button(root, text="Reset", fg='black', command=reset)
button1.place(x=25,y=140)
button2.place(x=100 , y = 140)
button3.place(x=175 , y = 140)
root.mainloop()   # Still Run untill to tell to stop