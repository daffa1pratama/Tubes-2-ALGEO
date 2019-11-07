from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import facerecog as main

def fileDialog():
    global canvasImg, sample
    sample = [filedialog.askopenfilename(initialdir =  path_uji, title = "Pilih Foto MukeGile", filetype =
    (("jpeg files","*.jpg"),("all files","*.*")))]
    photo = ImageTk.PhotoImage(Image.open(sample[0]))
    canvImg = Canvas(window,height=250,width=250)
    canvImg.place(x= 550, y = 400)
    canvImg.create_image(0,0,anchor='nw', image=photo)
    canvImg.image = photo
    sample[0] = sample[0].replace("/","\\")

def browse_uji():
    global path_uji
    filename = filedialog.askdirectory()
    path_uji.set(filename)

def browse_ref():
    global path_ref
    filename = filedialog.askdirectory()
    path_ref.set(filename)

def recognize():
    global T, select
    T = int(EntryJumlah.get())
    select = Metode.get()
    main.run(sample, T, select, path_uji, path_ref)

window=Tk()
window.geometry("750x750")
window.title("Face Recognition Bray")

window.config(bg="black")
folder_path = StringVar()
topn = StringVar()

labell = Label(window, text = "Welcome to Face Recognition", fg='black', bg ='blue' ,relief = 'solid', bd = 5, font=("arial",28,"bold")).pack()
LabelRecognizer = Label(window, text = "Made by MukeGile ©", fg='blue', bg ='black' ,relief = 'solid', bd = 5, font=("arial",18,"bold")).pack()
img = ImageTk.PhotoImage(Image.open("face.jpg"))
imglabel = Label(window, image=img).pack()
labelT = Label(window, text = "Masukkan Nilai T", fg='white', bg='black', relief='solid', font=('Arial', 10, 'bold'))
labelT.place(x=50, y=550)

button_sample=Button(window, text = "Browse Photo", fg='black', bg ='blue', activebackground = "black", command=fileDialog , relief = RAISED, bd = 2, font=("arial",15,"bold"))
button_sample.place(x=50, y=460)
button_uji=Button(window, text = "Browse Sample", fg='black', bg ='blue', relief = RAISED, bd = 2, font=("arial",15,"bold"), command=browse_uji)
button_uji.place(x=250, y=400)
button_ref=Button(window, text = "Browse Reference", fg='black', bg ='blue', relief = RAISED, bd = 2, font=("arial",15,"bold"), command=browse_ref)
button_ref.place(x=50, y=400)
button_recognize=Button(window, text = "RECOGNIZE ME!", fg='blue', bg ='black', command = recognize, relief = RAISED, bd = 2, font=("arial",15))
button_recognize.place(x=200, y=625)
LabelRecognizer = Label(window, text = "Select Recognizer :", fg='blue', bg ='black' ,relief = 'solid', bd = 5, font=("arial",15,"bold"))
LabelRecognizer.place(x=50, y= 500)
LabelHowMany = Label(window, text = "How many result do you want ?", fg='blue', bg ='black' ,relief = 'solid', bd = 5, font=("arial",10,"bold"))
LabelHowMany.place(x = 50, y = 595)

Metode = IntVar()

R1 = Radiobutton(window, 
              text="Cosine Similarity",
              padx = 30, 
              font=("arial",10,"italic"),
              activebackground = "black",
              activeforeground = "blue",
              bg = "black",
              fg = "blue",
              variable=Metode, 
              value=1)
R1.place(x=50, y= 540)
R2 = Radiobutton(window, 
              text="Euclidean Distance",
              font=("arial",10,"italic"),
              activebackground = "black",
              activeforeground = "blue",
              bg = "black",
              fg = "blue",
              padx = 30, 
              variable=Metode, 
              value=2)
R2.place(x=50, y= 570)

EntryJumlah = Entry(window)
EntryJumlah.place(x = 60, y = 630)



window.mainloop()
 
