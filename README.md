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

![image](https://github.com/user-attachments/assets/c86a5012-47cf-4c96-9f78-85429aa6bc2d)

# Data

Dataset berasal dari file glass.csv yang memuat fitur kimia dari kaca seperti:
1. RI (Refractive Index)
2. Na, Mg, Al, Si, K, Ca, Ba, Fe (Komposisi kimia)
3. Type (Label klasifikasi)

![image](https://github.com/user-attachments/assets/9ab855f7-551c-4176-95a6-095d7bd9d3b6)

![image](https://github.com/user-attachments/assets/663464a1-ab09-44bd-b6df-0b000a3a1125)

![image](https://github.com/user-attachments/assets/62f113a9-df1a-4668-943d-db24223defd5)

![image](https://github.com/user-attachments/assets/f5386567-7347-4674-8dfb-bca5833f673e)

![image](https://github.com/user-attachments/assets/80124d23-804c-41f9-b2aa-6797dad7d3f8)



#  Exploratory Data Analysis (EDA)

EDA mencakup:
1. Pemeriksaan struktur dan ringkasan data (info, describe, isnull)
2. Visualisasi korelasi antar fitur
3. Distribusi nilai fitur menggunakan histogram dan boxplot
4. Distribusi label Type menggunakan countplot
5. Analisis multivariat menggunakan pairplot

# Preprocessing


