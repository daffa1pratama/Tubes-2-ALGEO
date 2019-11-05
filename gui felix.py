import tkinter

from tkinter import filedialog
from tkinter import *

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

window = tkinter.Tk()
window.title("Face Recognition Application")


folder_path = StringVar()
welcome = Label(master=window,justify=LEFT, text='Face Recognition Program\nSteps:\nClick Browse Folder, then set the folder path.')
welcome.pack()
lbl1 = Label(master=window,textvariable=folder_path)
lbl1.pack()
lbl1.place()
button2 = Button(text="Browse Folder",justify=LEFT, command=browse_button)
button2.pack()
button2.place(anchor=NW)

close_btn = Button(window, text = "Close", command = window.quit) # closing the 'window' when you click the button
close_btn.pack(side = BOTTOM, fill = X)

mainloop()
