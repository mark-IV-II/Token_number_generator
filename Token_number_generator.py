#Token number generator

import os
import tkinter
from tkinter import ttk,Tk,messagebox,Menu,IntVar
from playsound import playsound

VERSION='2.1.0-beta'
TITLE='Token Number Generator '+VERSION #window title

root=Tk()

#global variables
num = IntVar()
audio_flag = IntVar()

#function to play notification sound when called
def playaudio(event=None):
    if audio_flag.get()==1:
        audio_path=os.path.join('.','notify','notify.mp3') #path to file is made os independent
        playsound(audio_path)
    
#function to increase the token number displayed by 1
def next_num(event=None):
    number=num.get()
    number+=1
    num.set(number)
    root.update()
    playaudio()

#function to decrease the token number displayed by 1
def prev_num(event=None):

    number=num.get()

    #making sure that number is always greater than 1 to avoid invalid token number being displayed
    if number > 1:
        number-=1
        num.set(number)
        root.update()
        playaudio()
    else:
        messagebox.showwarning('Warning','Minimum token number is 1')

#function to reset number and notification audio flag 
def reset():
    num.set(1)
    audio_flag.set(1)

#function to show help and about information in a new tkinter window
def about():
    
    window=Tk()
    window.title('Help & About')

    about_line = "Thank you for using Token Number Generator v"+VERSION+"\n(C) 2020 Aditya Anand under GPL v3.0 "

    help_line = "Press up arrow  key for next number\nPress down arrow key for previous number\nPress enter key to play the notification sound\nFor further queries connect via the github page"

    source_line = "Source code : https://github.com/mark-IV-II/Token_number_generator.git\nSound credits : https://www.soundbible.com"

    
    # Layout properties with weights for responsive UI 
    window.columnconfigure(0, weight=1, minsize=100)
    window.rowconfigure([0, 1, 2], weight=1, minsize=100)

    #Labels layout
    about_label = ttk.Label(window, text=about_line)
    about_label.config(font=('Calibri 10 bold'))
    about_label.grid(row=0,column=0,padx=10,pady=10)

    help_label = ttk.Label(window, text=help_line)
    help_label.config(font=('Calibri 12'))
    help_label.grid(row=1,column=0)
    
    source_label = ttk.Label(window, text=source_line)
    source_label.config(font=('Calibri 10 bold'))
    source_label.grid(row=2,column=0,padx=20,pady=20)
    


root.title(TITLE) #set window title

# create menubar to display menu and its options
menubar=Menu(root) 
root.config(menu=menubar)

reset() #set number and notification audio flag 

# keyboard shortcuts for easy operation
root.bind('<Up>',next_num) #press up arrow  key for next number
root.bind('<Down>',prev_num) #press down arrow key for previous number
root.bind('<Return>',playaudio) #press enter key to play the notification sound

# Layout properties with weights for responsive UI
root.columnconfigure(0, weight=2, minsize=150)
root.rowconfigure(1, weight=2, minsize=250)
root.columnconfigure([0, 2], weight=1, minsize=25)
root.rowconfigure(1, weight=2, minsize=50)

# Main label that displays the token number
number_label = ttk.Label(root, textvariable = num)
number_label.config(font=('Verdana 400 bold'))
number_label.grid(row=0,column=1)

# Buttons layout
next_button=ttk.Button(root, text = 'Next', width = 20, command=next_num)
next_button.grid(row=1,column=1,padx=10,pady=10)
back_button=ttk.Button(root, text = 'Back', width = 10,  command=prev_num)
back_button.grid(row=1,column=0,padx=10,pady=10)
notify_button=ttk.Button(root, text = 'Notify', width = 10, command=playaudio)
notify_button.grid(row=1,column=2, padx=10, pady=10)

# File menu 
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label='Reset', command=reset)
filemenu.add_command(label='Quit', command=root.quit)
menubar.add_cascade(label='File', menu=filemenu)

#Options menu
options = Menu(menubar, tearoff = 0)
options.add_checkbutton(label='Audio', variable=audio_flag)
options.add_command(label='Help', command=about)
menubar.add_cascade(label='Options', menu=options)

root.mainloop()