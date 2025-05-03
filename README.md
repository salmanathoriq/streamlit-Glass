# Glass Classification Project

Proyek ini bertujuan untuk melakukan klasifikasi jenis kaca berdasarkan komposisi kimianya.
dilakukan mulai dari eksplorasi data, preprocessing, pelatihan model machine learning,
hingga deployment sederhana menggunakan model yang telah disimpan.

# Library yang Digunakan

1. pandas, numpy: Untuk manipulasi data
2. matplotlib, seaborn: Untuk visualisasi
3. sklearn: Untuk preprocessing data, pelatihan model, evaluasi, dan pencarian hyperparameter
4. streamlit: Untuk pembuatan antarmuka interaktif (belum diimplementasikan penuh dalam kode)
5. pickle: Untuk menyimpan model

# Data

Dataset berasal dari file glass.csv yang memuat fitur kimia dari kaca seperti:
1. RI (Refractive Index)
2. Na, Mg, Al, Si, K, Ca, Ba, Fe (Komposisi kimia)
3. Type (Label klasifikasi)

![image](https://github.com/user-attachments/assets/f5386567-7347-4674-8dfb-bca5833f673e)


#  Exploratory Data Analysis (EDA)

EDA mencakup:
1. Pemeriksaan struktur dan ringkasan data (info, describe, isnull)
2. Visualisasi korelasi antar fitur
3. Distribusi nilai fitur menggunakan histogram dan boxplot
4. Distribusi label Type menggunakan countplot
5. Analisis multivariat menggunakan pairplot

# Preprocessing


