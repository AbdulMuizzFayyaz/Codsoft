from tkinter import *
import os

TITLE = 'To-do List'
GEOMETRY = '400x650'
BACKGROUND_COLOR = '#475a80'
#window
window = Tk()
window.title(TITLE)
window.geometry(GEOMETRY)
window.configure(bg=BACKGROUND_COLOR)
window.resizable(False,False)

#Task list.
task_list = []

#Task File.
TASKFILE = 'task.txt'

#Function to add task.
def addtask():
    task=entry.get()
    entry.delete(0, END)

    if task:
        with open(TASKFILE,'a') as taskfile:
            taskfile.write("\n")
        task_list.append(task)
        listbox.insert(END , task)

#Function to delete task.
def deletetask():
    global task_list

    task =str(listbox.get(ANCHOR))

    if task in task_list:
        task_list.remove(task)
        with open(TASKFILE,'w') as taskfile:
            taskfile.write('\n + task')
        
        listbox.delete(ANCHOR)

#Function to open task.txt
def opentaskfile():
    try:
        with open(TASKFILE,'r') as taskfile:
            tasks=taskfile.readlines()

        for task in tasks:
            if task != "\n":
                task_list.append(task)
                listbox.insert(END, task)
    except:
        if not os.path.isfile(TASKFILE):       
            with open(TASKFILE, "w") as f:     
                f.write("")


#Icon.
icon = PhotoImage(file='Image/icon.png')
window.wm_iconphoto(False,icon)

#Top bar.
top_bar = PhotoImage(file='Image/topbar.png')
top_bar_label = Label(window,
                      image=top_bar,
                      bg=BACKGROUND_COLOR)
top_bar_label.pack()

#Dock.
dock = PhotoImage(file='Image/dock.png')
dock_label = Label(window,
                   image= dock,
                   bg='#32405b')
dock_label.place(x=30,y=25)

#Note.
note_label = Label(window,
                   image=icon,
                   bg='#32405b')
note_label.place(x=340,y=20)

#Heading.
heading = Label(window,
                text= 'ALL TASK',
                font=('Monotype Corsiva','20','bold'),
                fg='white',
                bg='#32405b')
heading.place(x=130,y=25)

#Entry frame.
frame = Frame(window,
              width=400,
              height=50,
              bg='white')
frame.place(x=0,y=180)

#Tkinter string variable for task.
task = StringVar()

#Entry.
entry = Entry(frame,
              width=18,
              font= ('Monotype Corsiva','20'),
              bd=0)
entry.place(x=10, y=7)
entry.focus()

#Add button.
add = Button(frame,
             text='ADD',
             font=('Monotype Corsiva','20','bold'),
             width=6,
             bg='#5a95ff',
             fg='#fff',
             bd=0,
             command= addtask)
add.place(x=300,y=0)

#Listbox frame.
listbox_frame = Frame(window,
                      width=700,
                      height=280,
                      bd=3,
                      bg='#32405b')
listbox_frame.pack(pady=(160,0))

#Listbox.
listbox = Listbox(listbox_frame,
                  font=('Monotype Corsiva','12'),
                  width=45,
                  height=16,
                  bg='#32405b',
                  fg='white',
                  cursor='hand2',
                  selectbackground='#5a95ff')
listbox.pack(side='left',fill='both',padx=2)

#Scrollbar.
scroll_bar = Scrollbar(listbox_frame)
scroll_bar.pack(side='right',fill='both')

#Configuring listbox and scrollbar.
listbox.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=listbox.yview)

opentaskfile()

#Delete button.
delete = PhotoImage(file='Image/delete.png')
delete_button = Button(window,
                       image=delete,
                       bd=0,
                       bg=BACKGROUND_COLOR,
                       command=deletetask)
delete_button.pack(side='bottom',pady=13)

#Run.
window.mainloop()