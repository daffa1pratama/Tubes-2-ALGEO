import cv2
import numpy as np
import scipy 
from matplotlib.image import imread
import pickle as pickle
import random
import os
import matplotlib.pyplot as plt
from scipy import spatial
import math

# *** IMAGE EXTRACTOR *** #
# Image extractor memanfaatkan library OpenCV2
def extract_image(image_path, vector_size=32):
    # Extractor menggunakan fungsi yang terdapat pada KAZE
    image = imread(image_path)
    try:
        # * Konstruktor KAZE * #
        root = cv2.ORB_create()

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
            descriptor = np.concatenate([descriptor, np.zeros(needed_size - descriptor.size)])
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
        name = f.split('/')[-1]
        result[name] = extract_image(f)
    
    # Menyimpan semua vektor yang dibaca menjadi file database.pck
    # Memanfaatkan library pickle
    with open(pickled_db_path, 'wb') as fp:
        pickle.dump(result, fp)

# *** IMAGE MATCHER *** #
# Mencocokkan foto uji dengan foto referensi
class Matcher(object):

    # * Initiation * #
    def __init__(self, pickled_db_path):
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
def dotProduct(arrSample, arrReference):
    # Menghitung hasil perkalian dot product
    dot = 0
    for i in range(len(arrSample)):
        mul = arrSample[i]*arrReference[i]
        dot += mul
    return dot
def lenVector(vector):
    # Menghitung panjang vektor
    panjang = 0
    for i in range(len(vector)):
        power = pow(vector[i], 2)
        panjang += power
    return math.sqrt(panjang)
def cosine_similarity(arrSample, arrReference):
    # Menghitung kedekatan 2 vektor gambar dengan cosine similarity
    # Semakin mendekati 1, semakin mirip kedua gambar tersebut
    # Semakin mendekati 0, semakin tidak mirip kedua gambar tersebut
    cdist = dotProduct(arrSample, arrReference)/(lenVector(arrSample)*lenVector(arrReference))
    return cdist

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
        for i in range(len(arrReference)):
            cosine[i] = 1-cosine_similarity(arrSample, arrReference[i])
        cosine = np.array(cosine)
        print(cosine)
        return cosine

    else: # Euclidean Distance
        dist = [0 for i in range(len(arrReference))]
        for i in range(len(arrReference)):
            dist[i] = euclidean_distance(arrSample, arrReference[i])
        dist = np.array(dist)
        return dist

def sortTop(arrMatch, top):
    # Mengurutkan hasil yang paling cocok sebanyak topn
    near_id = np.argsort(arrMatch)[:top].tolist()
    return near_id

def show_img(path,i):
    # Menampilkan gambar ke layar
    img = imread(path)
    plt.imshow(img)
    plt.show()

def menu():
    print("Ada 2 metode pencocokan wajah")
    print("1. Cosine Similarity")
    print("2. Euclidean Distance")

def run(sample, T, select):
    path_uji = r"C:\Users\ASUS/Desktop\Database Tugas Besar\Data Uji"
    path_ref = r"C:\Users\ASUS/Desktop\Database Tugas Besar\Data Referensi"
    #path_uji = "..\pins-face-recognition\PINS\pins_zendaya"
    #path_ref = "..\pins-face-recognition\Pins\pins_zendaya"
    file_sample = [os.path.join(path_uji, p) for p in sorted(os.listdir(path_uji))]
    
    #batch_extractor(path_uji, "ujiorb.pck")
    #batch_extractor(path_ref, "referensiorb.pck")

    #uji = Matcher("uji.pck")
    #ref = Matcher("referensi.pck")
    uji = Matcher("ujiorb.pck")
    ref = Matcher("referensiorb.pck")

    print(sample[0])
    print(uji.names[100])

    # Get Index Sample
    # Mencari index sample di dalam array uji
    idSample = 0
    while(uji.names[idSample] != sample[0]):
        idSample += 1

    # Mencocokkan gambar uji dengan gambar referensi
    result = match(select, uji.vector[idSample], ref.vector)

    # Mencetak hasil gambar yang paling cocok sebanyak T gambar
    near_id = sortTop(result, T)

    for i in range(T):
        if(select==1):
            near_dist = 1-result[near_id[i]]
        elif(select==2):
            near_dist = result[near_id[i]]
        print(str(i+1) + ". " + ref.names[near_id[i]] + " : " + str(near_dist))
        #show_img(os.path.join(ref.names[near_id[i]]), i)
        img = imread(os.path.join(ref.names[near_id[i]]))
        plt.figure(i)
        plt.imshow(img)
    plt.show()