from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import facerecog as main

def fileDialog():
    global canvasImg, sample
    sample = [filedialog.askopenfilename(initialdir =  folder_path, title = "Pilih Foto MukeGile", filetype =
    (("jpeg files","*.jpg"),("all files","*.*")))]
    print(sample)
    photo = ImageTk.PhotoImage(Image.open(sample[0]))
    canvImg = Canvas(window,height=250,width=250)
    canvImg.place(x= 550, y = 400)
    canvImg.create_image(0,0,anchor='nw', image=photo)
    canvImg.image = photo

def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)

def getEntryTop():
    global T
    T = topn.get()
    label = Label(window, text=T)
    label.pack()

def runMain():
    main.run()

def selectCosine():
    global select
    select = 1

def selectEuclid():
    global select
    select = 2

window=Tk()
window.geometry("750x750")
window.title("Face Recognition Bray")

window.config(bg="black")
folder_path = StringVar()
topn = IntVar()
selMethod = IntVar()

labell = Label(window, text = "Welcome to Face Recognition", fg='black', bg ='blue' ,relief = 'solid', bd = 5, font=("Arial",28,"bold")).pack()
labelll = Label(window, text = "Made by MukeGile ©", fg='blue', bg ='black' ,relief = 'solid', bd = 5, font=("Arial",18,"bold")).pack()
img = ImageTk.PhotoImage(Image.open("face.jpg"))
imglabel = Label(window, image=img).pack()
labelT = Label(window, text = "Masukkan Nilai T", fg='white', bg='black', relief='solid', font=('Arial', 10, 'bold'))
labelT.place(x=50, y=550)

button1=Button(window, text = "Cari Foto!", fg='black', bg ='blue', activebackground = "black", command=fileDialog , relief = RAISED, bd = 2, font=("Arial",20,"bold"))
button1.place(x=50, y=400)
button2=Button(window, text = "Cari Folder!", fg='black', bg ='blue', relief = RAISED, command = browse_button, bd = 2, font=("Arial",20,"bold"))
button2.place(x=50, y=480)
button2=Button(window, text = "RECOGNIZE ME!", fg='blue', bg ='black', relief = RAISED, bd = 2, font=("Arial",28,"bold"), command=runMain)
button2.place(x=50, y=680)
button_cosine = Button(window, text = "Cosine Similarity", fg = 'black', bg = 'blue', relief = RAISED, font=("Arial",14,"bold"), command=selectCosine)
button_cosine.place(x=50, y=620)
button_euclid = Button(window, text = "Euclidean Distance", fg = 'black', bg = 'blue', relief = RAISED, font=("Arial",14,"bold"), command=selectEuclid)
button_euclid.place(x=300, y=620)

entryTop = Entry(window, textvariable=topn)
entryTop.place(x=50, y=580)
buttonTop = Button(window, command=getEntryTop, text="Enter")
buttonTop.place(x=250, y=575)

window.mainloop()
 
