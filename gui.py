import tkinter
from tkinter import filedialog
from tkinter import *
import os
from PIL import ImageTk, Image

def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)

def browse_file():
    global canv, filename
    filename = filedialog.askopenfilename(initialdir = folder_path, title = "Select File", filetype = (("jpeg files","*.jpg"),("all files","*.*")))
    photo = ImageTk.PhotoImage(Image.open(filename))
    canv = Canvas(window, height=1000, width=1000)
    canv.grid(columnspan=2, row=3)
    canv.create_image(20,20,anchor='nw',image=photo)
    canv.image=photo
    print(folder_path)
    print(filename)

window = Tk()
window.title("Face Recognition")

folder_path = StringVar()

main_title = Label(window, text="FACE RECOGNITION", font=24)
main_title.grid(row=0, columnspan=3, sticky='new')

browse_folder = Button(window, text="Browse File Directory", bg="red", font=30, command=browse_button)
browse_folder.grid(row=1, sticky='nsew')

browse_file = Button(window, text="Browse File", bg="blue", command=browse_file, font=30)
browse_file.grid(column=1, row=1, sticky='nsew')


window.mainloop()