# Glass Classification Project

Proyek ini bertujuan untuk melakukan klasifikasi jenis kaca berdasarkan komposisi kimianya.
dilakukan mulai dari eksplorasi data, preprocessing, pelatihan model machine learning,
hingga deployment sederhana menggunakan model yang telah disimpan.

# Library yang Digunakan

- pandas, numpy: Untuk manipulasi data
- matplotlib, seaborn: Untuk visualisasi
- sklearn: Untuk preprocessing data, pelatihan model, evaluasi, dan pencarian hyperparameter
- streamlit: Untuk pembuatan antarmuka interaktif (belum diimplementasikan penuh dalam kode)
- pickle: Untuk menyimpan model

![image](https://github.com/user-attachments/assets/c86a5012-47cf-4c96-9f78-85429aa6bc2d)

# Data

Dataset berasal dari file glass.csv yang memuat fitur kimia dari kaca seperti:
- RI (Refractive Index)
- Na, Mg, Al, Si, K, Ca, Ba, Fe (Komposisi kimia)
- Type (Label klasifikasi)

![image](https://github.com/user-attachments/assets/9ab855f7-551c-4176-95a6-095d7bd9d3b6)

![image](https://github.com/user-attachments/assets/663464a1-ab09-44bd-b6df-0b000a3a1125)

![image](https://github.com/user-attachments/assets/62f113a9-df1a-4668-943d-db24223defd5)

![image](https://github.com/user-attachments/assets/f5386567-7347-4674-8dfb-bca5833f673e)

![image](https://github.com/user-attachments/assets/80124d23-804c-41f9-b2aa-6797dad7d3f8)



#  Exploratory Data Analysis (EDA)

EDA mencakup:
- Pemeriksaan struktur dan ringkasan data (info, describe, isnull)
- Visualisasi korelasi antar fitur
- Distribusi nilai fitur menggunakan histogram dan boxplot
- Distribusi label Type menggunakan countplot
- Analisis multivariat menggunakan pairplot

![image](https://github.com/user-attachments/assets/e6526627-5539-4bc1-9604-9050590eacaa)

![image](https://github.com/user-attachments/assets/d12d4e25-f1d2-499d-bce7-ebc5bf6de751)

![image](https://github.com/user-attachments/assets/c41b8f20-fcce-4a1f-bc10-93c055eab89a)

![image](https://github.com/user-attachments/assets/236087a6-5689-4069-b1e2-37760f8c0cb2)



# Preprocessing

- Transformasi fitur menggunakan Yeo-Johnson PowerTransformer
- Pembagian data: 80% untuk pelatihan, 20% untuk pengujian
- Standardisasi fitur menggunakan StandardScaler

![image](https://github.com/user-attachments/assets/61e97fbf-4fa6-48f9-87cc-57de9b35f2a9)

![image](https://github.com/user-attachments/assets/44b9fe67-c4f3-4978-9568-1fd411980eed)

![image](https://github.com/user-attachments/assets/631b6941-1a39-4f88-8862-860ea83ca2db)

# Modeling

1. K-Nearest Neighbors (KNN)
   - Evaluasi menggunakan confusion matrix, accuracy, precision, dan classification report
   - Pencarian hyperparameter terbaik menggunakan GridSearchCV
2. Linear Regression
   - Digunakan untuk prediksi sederhana dan sebagai baseline
   - Evaluasi dengan score pada data uji

![image](https://github.com/user-attachments/assets/f5b2168b-8189-468d-ba18-cb1644017099)

![image](https://github.com/user-attachments/assets/6c745c9c-7943-4f69-8f6d-4b45f7de95e6)

![image](https://github.com/user-attachments/assets/4ee20102-dfa9-4542-bf5b-c86c3f3ded25)


#  Prediksi Data Baru

Model linier digunakan untuk prediksi jenis kaca dari data baru. Contoh data input:

![image](https://github.com/user-attachments/assets/97e3a045-ba66-494a-8d80-8dfdc91fae4a)

# Menyimpan Model

Model regresi linier disimpan menggunakan pickle untuk kebutuhan deployment:

![image](https://github.com/user-attachments/assets/278b61bf-0773-4e04-808d-a8dbc7c6644f)

# Catatan

- Model terbaik untuk klasifikasi kemungkinan bukan regresi linier; KNN memiliki performa lebih baik.
- Streamlit sudah di-import tetapi belum digunakan secara eksplisit dalam kode ini.
- Disarankan untuk membuat antarmuka Streamlit agar user dapat melakukan prediksi langsung dengan menginput data mereka sendiri.









