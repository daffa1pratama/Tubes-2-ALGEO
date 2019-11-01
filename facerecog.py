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
# Image extractor ini memanfaatkan library OpenCV2
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


def batch_extractor(images_path, pickled_db_path="features.pck"):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    result = {}
    for f in files:
        print ("Extracting features from image %s" % f)
        name = f.split('/')[-1].lower()
        result[name] = extract_image(f)
    
    # saving all our feature vectors in pickled file
    with open(pickled_db_path, 'wb') as fp:
        pickle.dump(result, fp)

class Matcher(object):

    def __init__(self, pickled_db_path="features.pck"):
        with open(pickled_db_path, 'rb') as fp:
            self.data = pickle.load(fp)
        self.names = []
        self.matrix = []
        for k, v in self.data.items():
            self.names.append(k)
            self.matrix.append(v)
        self.matrix = np.array(self.matrix)
        self.names = np.array(self.names)

    def cos_cdist(self, vector):
        # getting cosine distance between search image and images database
        v = vector.reshape(1, -1)
        return scipy.spatial.distance.cdist(self.matrix, v, "cosine").reshape(-1)

    def match(self, image_path, topn=5):
        features = extract_image(image_path)
        img_distances = self.cos_cdist(features)
        # getting top 5 records
        nearest_ids = np.argsort(img_distances)[:topn].tolist()
        nearest_img_paths = self.names[nearest_ids].tolist()

        return nearest_img_paths, img_distances[nearest_ids].tolist()


def cosine_similarity(arrsample, arrextract):
    dot=0
    for i in range(len(arrsample)):
        dotopr = arrsample[i]*arrextract[i]
        dot += dotopr
    normsample = 0
    for i in range(len(arrsample)):
        x = arrsample[i]**2
        normsample += x
    normextract = 0
    for i in range(len(arrsample)):
        x = arrextract[i]**2
        normextract += x
    normsample = normsample**0.5
    normextract = normextract**0.5
    return(dot/(normextract*normsample))

def euclidean_distance(arrsample, arrextract):
    sum=0
    temp=0
    for i in range(len(arrsample)):
        temp = (arrsample[i] - arrextract[i])**2
        sum += temp
    return(sum**0.5)

def show_img(path):
    img = imread(path)
    plt.imshow(img)
    plt.show()