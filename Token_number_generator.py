#Token number generator

import tkinter
from tkinter import ttk,Tk,Canvas
from playsound import playsound

def playaudio():
    playsound('.\\notify\\notify.mp3')

def next_num(event=None):
    number=num.get()
    number+=1
    num.set(number)
    root.update()
    playaudio()

def prev_num(event=None):
    number=num.get()
    if number > 1:
        number-=1
    num.set(number)
    root.update()
    playaudio()


root=Tk()

root.title('Token Number Generator')
root.bind('<Return>',next_num)
root.bind('<Shift-Return>',prev_num)

app_canvas= Canvas(root, width = 1024, height = 768)
app_canvas.pack()

num = tkinter.IntVar()
num.set(1)

number_label = ttk.Label(root, textvariable = num)
number_label.config(font=('Verdana 400 bold'))

next_button=ttk.Button(root, text = 'Next', width = 20, command=next_num)
back_button=ttk.Button(root, text = 'Back', width = 10,  command=prev_num)
notify_button=ttk.Button(root, text = 'Notify', width = 10, command=playaudio)

app_canvas.create_window(512,360,window=number_label)
app_canvas.create_window(500,750,window=next_button)
app_canvas.create_window(125,750,window=back_button)
app_canvas.create_window(900,750,window=notify_button)

root.mainloop()
