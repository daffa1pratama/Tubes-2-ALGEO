from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

def fileDialog():
    global canv, filename
    filename = filedialog.askopenfilename(initialdir =  folder_path, title = "Pilih Foto MukeGile", filetype =
    (("jpeg files","*.jpg"),("all files","*.*")) )
    photo = ImageTk.PhotoImage(Image.open(filename))
    canv = Canvas(window,height=300,width=300)
    canv.place(x= 400, y = 400)
    canv.create_image(20,20,anchor='nw', image=photo)
    canv.image = photo


class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.defaultForeground = self['foreground']
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']
        self['foreground'] = self['activeforeground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
        self['foreground'] = self.defaultForeground

def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)

window=Tk()
window.geometry("750x750")
window.title("Face Recognition Bray")
window.config(bg="black")
folder_path = StringVar()

labell = Label(window, text = "Welcome to Face Recognition", fg='black', bg ='blue' ,relief = 'solid', bd = 5, font=("arial",28,"bold")).pack()
LabelRecognizer = Label(window, text = "Made by MukeGile ©", fg='blue', bg ='black' ,relief = 'solid', bd = 5, font=("arial",18,"bold")).pack()
img = ImageTk.PhotoImage(Image.open("face.jpg"))
imglabel = Label(window, image=img).pack()



button1=Button(window, text = "Cari Foto!", fg='black', bg ='blue', activebackground = "black", command=fileDialog , relief = RAISED, bd = 2, font=("arial",20,"bold"))
button1.place(x=50, y=400)
button2=Button(window, text = "Cari Folder!", fg='black', bg ='blue', relief = RAISED, command = browse_button, bd = 2, font=("arial",20,"bold"))
button2.place(x=50, y=460)
LabelRecognizer = Label(window, text = "Select Recognizer :", fg='blue', bg ='black' ,relief = 'solid', bd = 5, font=("arial",22,"bold"))
LabelRecognizer.place(x=50, y= 510)
LabelHowMany = Label(window, text = "How Many Muke you want to cari brow?!?", fg='blue', bg ='black' ,relief = 'solid', bd = 5, font=("arial",10,"bold"))
LabelHowMany.place(x = 50, y = 630)

v = IntVar()
def ShowChoice():
    print(v.get())
    global inputselect
    inputselect = v.get()


R1 = Radiobutton(window, 
              text="Cosine Similarity",
              padx = 40, 
              font=("arial",15,"italic"),
              activebackground = "black",
              activeforeground = "blue",
              bg = "black",
              fg = "blue",
              indicator = 0,
              variable=v, 
              value=1)
R1.place(x=50, y= 550)
R2 = Radiobutton(window, 
              text="Euclidean Distance",
              font=("arial",15,"italic"),
              activebackground = "black",
              activeforeground = "blue",
              bg = "black",
              fg = "blue",
              indicator = 0,
              padx = 40, 
              variable=v, 
              value=2)
R2.place(x=50, y= 590)
#button3=Button(window, text = "RECOGNIZE ME!", fg='blue', bg ='black', relief = RAISED, bd = 2, font=("arial",28,"bold"))
#button3.place(x=50, y=580)

window.mainloop()
 
