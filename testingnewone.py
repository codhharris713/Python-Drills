from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil
#tkinter widgets
def widgets():
    lbl = Label(root ,text="Files to Copy")
    lbl.grid(row= 1 ,column = 0)

    root.src_txt = Entry(root, textvariable = src_location)
    root.src_txt.grid(row= 1,column = 1)

    btn_src = ttk.Button(root, text = "Browse Folder", command = src)
    btn_src.grid(row=1,column=3)

    lbl = Label(root ,text="Destination Folder")
    lbl.grid(row= 2 ,column = 0)

    root.dest_txt = Entry(root, textvariable = dest_location)
    root.dest_txt.grid(row= 2,column = 1)

    btn_dest = ttk.Button(root, text = "Browse Folder", command = dest)
    btn_dest.grid(row=2,column=3)

    copy_btn = Button(root, text = "Copy Files", command = copy)
    copy_btn.grid(row=3, column=1)

#using askopenfilename to select files to copy
def src():
    root.src_files = filedialog.askopenfilenames()
    root.src_txt.insert('1',root.src_files)
    
#using askopendirectory to send the files that are being copied
def dest():
    dest_selected = filedialog.askdirectory()
    root.dest_txt.insert('1', dest_selected)
    
#copying files from the src to the dest folder using shutil.copy method
def copy():
    src_files = root.src_files
    dest_folder = dest_location.get()

    for i in src_files:
        shutil.copy(i, dest_folder)

root = Tk()
root.geometry("400x400")
root.title("Move Files")
#tkinter variable 
src_location = StringVar()
dest_location = StringVar()

widgets()

root.mainloop()
