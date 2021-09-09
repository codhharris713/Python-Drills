from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

gui = Tk()
gui.geometry("400x400")
gui.title("FC")
#class that contains all prop and fun for selecting a folder
class FolderSelect(Frame):
    def __init__(self,parent=None,folderDescription="",**kw):
        Frame.__init__(self,master=parent,**kw)
        self.folderPath = StringVar()
        self.lblName = Label(self, text=folderDescription)
        self.lblName.grid(row=0,column=0)
        self.entPath = Entry(self, textvariable=self.folderPath)
        self.entPath.grid(row=0,column=1)
        self.btnFind = ttk.Button(self, text="Browse Folder",command=self.setFolderPath)
        self.btnFind.grid(row=0,column=2)
    def setFolderPath(self):
        folder_selected = filedialog.askdirectory()
        self.folderPath.set(folder_selected)
    
    def folder_path(self):
        return self.folderPath.get()
#runs file check from test file move
def filecheck():
    os.system('test_file_move.py') 
    

folderPath = StringVar()

directory1Select = FolderSelect(gui,"Select Folder 1")
directory1Select.grid(row=0)

directory2Select = FolderSelect(gui,"Select Folder 2")
directory2Select.grid(row=1)



c = ttk.Button(gui, text="file check", command=filecheck)
c.grid(row=4,column=0)
gui.mainloop()
