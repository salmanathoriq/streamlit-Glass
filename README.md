# Glass Classification Project

Proyek ini bertujuan untuk melakukan klasifikasi jenis kaca berdasarkan komposisi kimianya.
dilakukan mulai dari eksplorasi data, preprocessing, pelatihan model machine learning,
hingga deployment sederhana menggunakan model yang telah disimpan.

# Library yang Digunakan

> pandas, numpy: Untuk manipulasi data
> matplotlib, seaborn: Untuk visualisasi
> sklearn: Untuk preprocessing data, pelatihan model, evaluasi, dan pencarian hyperparameter
> streamlit: Untuk pembuatan antarmuka interaktif (belum diimplementasikan penuh dalam kode)
> pickle: Untuk menyimpan model

# Data

Dataset berasal dari file glass.csv yang memuat fitur kimia dari kaca seperti:
> RI (Refractive Index)
> Na, Mg, Al, Si, K, Ca, Ba, Fe (Komposisi kimia)
> Type (Label klasifikasi)

#  Exploratory Data Analysis (EDA)

EDA mencakup:
> Pemeriksaan struktur dan ringkasan data (info, describe, isnull)
> Visualisasi korelasi antar fitur
> Distribusi nilai fitur menggunakan histogram dan boxplot
> Distribusi label Type menggunakan countplot
> Analisis multivariat menggunakan pairplot

