from tkinter import *
import webbrowser


#define function 
def web_browser():
    #open file for writing
    f = open('index.html','w')
    #getting value from message
    text = source.get()
    message = "<html><body><h1>%s</h1></body</html>" % text
    #write to file from message
    f.write(message)
    #close file
    f.close()
    #open new tab in browser
    webbrowser.open_new_tab('index.html')

root = Tk() #create window
source = StringVar()


root.geometry('500x500+500+500')
root.title('Make Your Own Text')
root.config(bg='red')

wblabel = Label(root,text='Type Your Text Below').pack() #create a text label

wbbutton = Button(root,text="Open in Browser",command = web_browser).pack() #create button that opens new page

wbEntry = Entry(root,textvariable=source).pack() #entry widget to display user input

