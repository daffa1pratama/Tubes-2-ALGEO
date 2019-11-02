import cv2
import numpy as np
import scipy 
from matplotlib.image import imread
import pickle as pickle
import random
import os
import matplotlib.pyplot as plt
from scipy import spatial

# *** IMAGE EXTRACTOR *** #
# Image extractor memanfaatkan library OpenCV2
def extract_image(image_path, vector_size=32):
    # Extractor menggunakan fungsi yang terdapat pada KAZE
    image = imread(image_path)
    try:
        # * Konstruktor KAZE * #
        root = cv2.KAZE_create()

        # * Detector keypoint * #
        # Membentuk keypoints yang terdapat pada foto wajah
        # Keypoints dibentuk berdasarkan ukuran gambar dan warna dari gambar dan terurut mengecil
        detector = root.detect(image)   
        detector = sorted(detector, key=lambda x: -x.response)[:vector_size]

        # * Computing descriptor * #
        # Menghitung vektor descriptor
        # Membentuk vektor-vektor tersebut menjadi vektor besar berukuran 2048 elemen berukuran sama
        detector, descriptor = root.compute(image, detector)
        descriptor = descriptor.flatten()
        needed_size = (vector_size * 64)
        if descriptor.size < needed_size:
            # Jika terdapat hanya 32 descriptor, vektor sisanya dibuat 0
            descriptor = np.concatenate([dsc, np.zeros(needed_size - descriptor.size)])
    except cv2.error as e:
        print ("Error: ", e)
        return None
    return descriptor

# *** DATABASE PACKAGE *** #
# Paket database dibungkus menjadi file database.pck
def batch_extractor(images_path, pickled_db_path):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
        # Membaca direktori image dan dimasukkan ke files=array[]

    result = {}
    for f in files:
        # Membaca seluruh isi gambar dan dimasukkan ke result=array[] sebagai database in array 
        print ("Extracting features from image %s" % f)
        name = f.split('/')[-1].lower()
        result[name] = extract_image(f)
    
    # Menyimpan semua vektor yang dibaca menjadi file database.pck
    # Memanfaatkan library pickle
    with open(pickled_db_path, 'wb') as fp:
        pickle.dump(result, fp)

# *** IMAGE MATCHER *** #
# Mencocokkan foto uji dengan foto referensi
class Matcher(object):

    # * Initiation * #
    def __init__(self, pickled_db_path="database.pck"):
        # Membentuk array vector dan array names
        with open(pickled_db_path, 'rb') as fp:
            self.data = pickle.load(fp)
        self.names = []
        self.vector = []
        for k, v in self.data.items():
            self.names.append(k)
            self.vector.append(v)
        self.vector = np.array(self.vector)
        self.names = np.array(self.names)

# *** VECTOR OPERATION *** #
# * Cosine Similarity * #
def cosine_similarity(arrSample, arrReference):
    # Menghitung kedekatan 2 vektor gambar dengan cosine similarity
    # Semakin mendekati 1, semakin mirip kedua gambar tersebut
    # Semakin mendekati 0, semakin tidak mirip kedua gambar tersebut
    dot=0
    for i in range(len(arrSample)):
        muldot = arrSample[i]*arrReference[i]
        dot += muldot
    lenSample = 0
    for i in range(len(arrSample)):
        x = arrSample[i]**2
        lenSample += x
    lenReference = 0
    for i in range(len(arrSample)):
        x = arrReference[i]**2
        lenReference += x
    lenSample = lenSample**0.5
    lenReference = lenReference**0.5
    return(dot/(lenReference*lenSample))

# * Euclidean Distance * #
def euclidean_distance(arrSample, arrReference):
    # Menghitung kedekatan 2 vektor gambar dengan euclidean distance
    # Semakin kecil nilai jarak, semakin mirip kedua gambar tersebut
    # Semakin besar nilai jarak, semakin tidak mirip kedua gambar tersebut
    sum=0
    temp=0
    for i in range(len(arrSample)):
        temp = (arrSample[i] - arrReference[i])**2
        sum += temp
    return(sum**0.5)

def match(operation, arrSample, arrReference):
    # Memilah gambar referensi yang cocok dengan gambar uji
    if(operation==1): # Cosine Similarity
        cosine = [0 for i in range(len(arrReference))]
        for i in range(len(arrSample)):
            cosine[i] = 1-cosine_similarity(arrSample, arrReference[i])
        cosine = np.array(cosine)
    else if(operation==2):  # Euclidean Distance
        dist = [0 for i in range(len(arrReference))]
        for i in range(len(arrReference)):
            dist[i] = euclidean_distance(arrSample, arrReference[i])
        dist = np.array(dist)

    features = extract_image(image_path)
    img_distances = self.cos_cdist(features)
    # getting top 5 records
    nearest_ids = np.argsort(img_distances)[:topn].tolist()
    nearest_img_paths = self.names[nearest_ids].tolist()

    return nearest_img_paths, img_distances[nearest_ids].tolist()

def show_img(path):
    # Menampilkan gambar ke layar
    img = imread(path)
    plt.imshow(img)
    plt.show()

def menu():
    print("Ada 2 metode pencocokan wajah")
    print("1. Cosine Similarity")
    print("2. Euclidean Distance")

def run():
    images_path = "..\pins-face-recognition\PINS\pins_zendaya"
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    
    batch_extractor(images_path, "uji.pck")
    batch_extractor(images_path, "referensi.pck")


    uji = Matcher("uji.pck")
    ref = Matcher("referensi.pck")

    
    print("===========================================")
    print("SELAMAT DATANG DI APLIKASI FACE RECOGNITION")
    print("===========================================")
    print()
    menu()
    loop = True
    while(loop):
        select = input("Masukkan pilihan metode pencocokan")
        if(select==1 | select==2):
            # Mendapatkan gambar uji secara acak
            sample = random.sample(files, 1)
            # Get Index Sample
            # Mencari index sample di dalam array uji
            idSample = 0
            while(uji.names[idSample] != sample[0].lower()):
                idSample += 1
            # Mencocokkan gambar uji dengan gambar referensi
            match(select, uji.vector[idSample], ref.vector)
        else if(select==3):
            loop=False
        else:
            print("Pilihan salah")
    