from tkinter import *
import ttkbootstrap as ttk
import random
from ttkbootstrap.dialogs import Messagebox

#Creating a list for uppercase alphabets.
uppercase_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Creating a list for lowercase alphabets.
lowercase_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Creating a list for numbers.
number = ['0','1','2','3','4','5','6','7','8','9']

#Creating a list for characters
characters = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','{','}','[',']',':',';',',','"',"'",'.','<','>']

#Combining the four lists into one.
combined = uppercase_alphabets+lowercase_alphabets+number+characters

#Function for generating password.
def password_gen():
    password=''
    try:
        for i in range(entry_int.get()):
            password+=random.choice(combined)
            output_string.set(password)
    except:
        Messagebox.show_error("Please enter a valid integer!","Invalid Input!")

TITLE = 'Password Generator'
GEOMETRY = '1000x200'
THEME = 'darkly'
#Window
window= ttk.Window(themename=THEME)
window.title(TITLE)
window.geometry(GEOMETRY)

#Icon
icon = PhotoImage(file = 'icon.png')
window.wm_iconphoto(False, icon)

#Title
title_label=Label(window,
                  text='Password Generator',
                  font=('Monotype Corsiva', '24' ,'bold'))
title_label.pack()

#Instruction label.
instruction = Label(window,
                    text='Enter the lenght of the password you want to generate',
                    font=('Monotype Corsiva', '12'))
instruction.pack(pady=5)

#Input field
input_frame=Frame(window)
entry_int=IntVar()
entry=Entry(input_frame, 
            textvariable=entry_int)
entry.focus()

#Generate button.
button = Button(input_frame,
                text='Generate',
                font=('Monotype Corsiva','12'),
                command=password_gen)

#Packing the entry and generate button by side.
entry.pack(side='left',padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

#Output for generated password.
output_string=StringVar()
output_label=Label(window,
                   font=('Monotype Corsiva' , '20'),
                   textvariable=output_string)
output_label.pack(pady=5)

#Run
window.mainloop()