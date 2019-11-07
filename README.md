# TUGAS BESAR 2 ALJABAR LINEAR DAN GEOMETRI
[Face Recognition]

Kelompok Muke Gile :
1. Daffa Pratama Putra          13518033
2. Radhinansyah Hemsa Ghaida    13518087
3. Fabianus Harry Setiawan      13518144

# Gambaran Program
Program ini dibuat menggunakan bahasa python dengan penggunaan library-library yang tersedia di dalamnya. Library yang digunakan antara lain :
- OpenCV
- Matplotlib
- Pillow
- Tkinter
- Scipy
- Numpy \n
Secara garis besar, program ini dapat mencocokkan gambar wajah seseorang dengan gambar wajah lain atau yang kini dikenal dengan teknologi Face Recognition atau Pengenalan Wajah. Face Recognition yang diimplementasikan dalam program ini menggunakan library OpenCV untuk mengekstraksi gambar wajah menjadi titik-titik vektor. Vektor tersebut nantinya akan dibandingkan dengan vektor pada gambar lain dengan metode cosine similarity dan euclidean distance. Program akan menampilkan hasil gambar termirip dengan gambar uji yang diberikan pengguna

*Program ini tidak sesempurna Face Recognition pada Machine Learning, sehingga seringkali terjadi ketidakcocokan dalam menggunakan program.

# Langkah Menggunakan Program
Berikut adalah langkah-langkah menggunakan program :
1. Jalankan gui.py pada terminal yang sudah terinstall python versi 3
2. Tekan tombol "Browse Reference" untuk menentukan lokasi folder referensi
3. Tekan tombol "Browse Sample" untuk menentukan lokasi folder uji
4. Tekan tombol "Browse Image" untuk menentukan gambar yang akan diuji (gambar sampel)
5. Pilih metode hitung yang digunakan dengan memencet bulatan di samping tulisannya
6. Masukkan banyak hasil yang ingin ditampilkan oleh program
7. Tekan tombol "Recognize Me" untuk menjalankan program
8. Tunggu sebentar, karena program akan mengekstraksi dan menghitung
9. Program akan memunculkan window baru untuk memperlihatkan hasil kecocokan
