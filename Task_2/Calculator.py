from tkinter import *

#Function for takign input from button.
def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

#Function for evaluating,with exception handling.
def equal():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("Syntax Error!")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("Cannot divide by 0!")
        equation_text = ""

#Function for clearing the label.
def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

TITLE = 'Calculator'
GEOMETRY = '600x600'
BACKGROUND_COLOR = '#42a19d'
#Window
window = Tk()
window.configure(bg=BACKGROUND_COLOR)
window.geometry(GEOMETRY)
window.title(TITLE)

#Icon
icon = PhotoImage(file = 'icon.png')
window.wm_iconphoto(True, icon)

#Empty string for equation text.
equation_text = ""

#Tkinter string variable for main label of calculator.
equation_label = StringVar()

#Frame for label which will give it a black border.
label_frame = Frame(window, 
                    bd=2, 
                    relief=SOLID, 
                    borderwidth=2, 
                    highlightbackground='black')
label_frame.pack(pady=10)

#Main label.
label = Label(label_frame, 
              textvariable=equation_label, 
              font=('Monotype Corsiva',20), 
              width=30, 
              height=3)
label.pack()

#A frame for buttons with black border.
button_frame= Frame(window, 
                    bd=2, 
                    relief=SOLID, 
                    borderwidth=2, 
                    highlightbackground='black')

#Configuring columns in frame for grid of buttons.
button_frame.columnconfigure(0,weight=1)
button_frame.columnconfigure(1,weight=1)
button_frame.columnconfigure(2,weight=1)
button_frame.columnconfigure(3,weight=1)

BUTTON_COLOR = '#b25dc7'
#Buttons for (0-9), (+,-,*,/), (=,.) .
btn1 = Button(button_frame,
              text='1',
              font=35, 
              height=4, 
              width=9,
              bg=BUTTON_COLOR,
              command=lambda:button_press(1))
btn1.grid(row=0,column=0,sticky='we')

btn2 = Button(button_frame,
              text='2',
              font=35, 
              height=4, 
              width=9,
              bg=BUTTON_COLOR,
              command=lambda:button_press(2))
btn2.grid(row=0,column=1,sticky='we')

btn3 = Button(button_frame,
              text='3',
              font=35, 
              height=4, 
              width=9,
              bg=BUTTON_COLOR,
              command=lambda:button_press(3))
btn3.grid(row=0,column=2,sticky='we')

btn4 = Button(button_frame,
              text='4',
              font=35, 
              height=4, 
              width=9,
              bg=BUTTON_COLOR,
              command=lambda:button_press(4))
btn4.grid(row=1,column=0,sticky='we')

btn5 = Button(button_frame,
              text='5',
              font=35, 
              height=4, 
              width=9,
              bg=BUTTON_COLOR,
              command=lambda:button_press(5))
btn5.grid(row=1,column=1,sticky='we')

btn6 = Button(button_frame,
              text='6',
              font=35, 
              height=4, 
              width=9,
              bg=BUTTON_COLOR,
              command=lambda:button_press(6))
btn6.grid(row=1,column=2,sticky='we')

btn7 = Button(button_frame,
              text='7',
              font=35, 
              height=4, 
              width=9,
              bg=BUTTON_COLOR,
              command=lambda:button_press(7))
btn7.grid(row=2,column=0,sticky='we')

btn8 = Button(button_frame,
              text='8',
              font=35, 
              height=4, 
              width=9,
              bg=BUTTON_COLOR,
              command=lambda:button_press(8))
btn8.grid(row=2,column=1,sticky='we')

btn9 = Button(button_frame,
              text='9',
              font=35, 
              height=4, 
              width=9,
              bg=BUTTON_COLOR,
              command=lambda:button_press(9))
btn9.grid(row=2,column=2,sticky='we')

btn0 = Button(button_frame,
              text='0',
              font=35, 
              height=4, 
              width=9,
              bg=BUTTON_COLOR,
              command=lambda:button_press(0))
btn0.grid(row=3,column=1,sticky='we')

btn_plus = Button(button_frame,
                  text='+',
                  font=35, 
                  height=4, 
                  width=9,
                  bg=BUTTON_COLOR,
              command=lambda:button_press('+'))
btn_plus.grid(row=0,column=3,sticky='we')

btn_minus = Button(button_frame,
                   text='-',
                   font=35, 
                   height=4, 
                   width=9,
                   bg=BUTTON_COLOR,
              command=lambda:button_press('-'))
btn_minus.grid(row=1,column=3,sticky='we')

btn_multiply = Button(button_frame,
                      text='x',
                      font=35, 
                      height=4, 
                      width=9,
                      bg=BUTTON_COLOR,
              command=lambda:button_press('*'))
btn_multiply.grid(row=2,column=3,sticky='we')

btn_divide = Button(button_frame,
                    text='÷',
                    font=35, 
                    height=4, 
                    width=9,
                    bg=BUTTON_COLOR,
              command=lambda:button_press('/'))
btn_divide.grid(row=3,column=3,sticky='we')

btn_decimal = Button(button_frame,
                     text='.',
                     font=35, 
                     height=4, 
                     width=9,
                     bg=BUTTON_COLOR,
              command=lambda:button_press('.'))
btn_decimal.grid(row=3,column=0,sticky='we')

btn_equals_to = Button(button_frame,
                       text='=',
                       font=35, 
                       height=4, 
                       width=9,
                       bg=BUTTON_COLOR,
              command=lambda:equal())
btn_equals_to.grid(row=3,column=2,sticky='we')

#Packing the button frame which contains the grid of buttons.
button_frame.pack(fill='x')

#Creating a clear button.
clear = Button(window, 
               text='Clear', 
               height=4, 
               width=15, 
               font=35,
               bg=BUTTON_COLOR,
               bd=2, 
               relief=SOLID, 
               highlightthickness=2, 
               highlightbackground="black",
             command=clear)
clear.pack(pady=10)

#Run
window.mainloop()