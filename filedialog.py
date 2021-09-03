import sys
import os
from tkinter import filedialog
from tkinter import *
#function for looking at folder A 
def browse():
    global folder_path
    filename = filedialog.askopenfilename(initialdir="/Users/Cody/Desktop/folder_A/", title="Select file",
                    filetypes=(("txt files", "*.txt"),("all files", "*.*")))


    folder_path.set(filename)
    print(filename)

def browse_2():
    global folder_path
    filename = filedialog.askopenfilename(initialdir="/Users/Cody/Desktop/folder_B/", title="Select file",
                    filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    folder_path.set(filename)
    print(filename)


    
#function for file check
def run():
    os.system('test_file_move.py')

root = Tk()
folder_path = StringVar()
lbll = Label(master=root,textvariable=folder_path)
lbll.grid(row=0, column=1)

#button to check file A
button = Button(text="File A", command=browse)
button.grid(row=0, column=3)

#button to check file B
button = Button(text="File B", command=browse_2)
button.grid(row=1, column=2)

#button for manual file check
button_1 = Button(text="Run File Check", command=run)
button_1.grid(row=2, column=5)

mainloop()
