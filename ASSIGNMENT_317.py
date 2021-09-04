import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def openFolder():
    tf = filedialog.askopenfilename(
        initialdir="/Users/Cody/Desktop/folder_A/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read() #read file
    txtarea.insert(END, data) #insert text from text.doc when file is clicked
    tf.close()

def openFolder_2():
    tf = filedialog.askopenfilename(
        initialdir="/Users/Cody/Desktop/folder_B/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf)  
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()

def run():
    os.system('test_file_move.py') #runs file check from test file move
    messagebox.showinfo('info', 'New and Edited files have been moved from Folder A to Folder B')

def clear_textbox():
    txtarea.delete(1.0, 'end')
         
ws = Tk()
ws.title("Read and Run File check on File A and File B")
ws.geometry("800x450")
ws['bg']='black'




txtarea = Text(ws, width=40, height=20)
txtarea.pack(pady=20)

pathh = Entry(ws)
pathh.pack(side=RIGHT, expand=True, fill=X, padx=20)


#open Folder A
Button(
    ws, 
    text="Open Folder A", 
    command=openFolder
    ).pack(side=LEFT, expand=True, fill=X, padx=20)
#open Folder B 
Button(
    ws, 
    text="Open Folder B", 
    command=openFolder_2
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)
#run file check
Button(
    ws, 
    text="Run File Check", 
    command=run
    ).pack(side=TOP, expand=True, fill=X, padx=20)

#clear text box
Button(
    ws,
    text='Clear',
    width=15,
    height=2,
    command=clear_textbox
    ).pack(expand=True)


ws.mainloop()
