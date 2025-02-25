## Pendahuluan

Tools ini dibuat untuk melakukan pengujian beban yang memungkinkan Anda mensimulasikan sejumlah besar pengguna
secara bersamaan untuk menguji kinerja aplikasi web Anda. Repository ini menyediakan kerangka kerja
dan skrip yang diperlukan untuk menjalankan pengujian beban menggunakan Locust.

## Struktur Direktori
**Locust/**  
**├── config/**  
**├── reports/**  
**├── tests/**  
**├── utils/**  
**├── .gitignore**  
**├── locustfile.py**  
**└── requirements.txt**

- **config/**    : Berisi file konfigurasi untuk pengujian.
- **reports/**   : Folder ini akan menyimpan laporan hasil pengujian.
- **tests/**     : Berisi skrip-skrip pengujian.
- **utils/**     : Berisi utilitas atau fungsi pendukung untuk pengujian.
- **locustfile.py** : Skrip utama yang mendefinisikan perilaku pengguna untuk pengujian beban.
- **requirements.txt** : Daftar dependensi atau pustaka yang diperlukan untuk menjalankan proyek ini.

## Persyaratan Sistem

Sebelum memulai, pastikan sistem Anda memiliki:

- **Python 3.7 atau lebih baru** : Locust membutuhkan Python versi terbaru.
- **Pustaka yang tercantum dalam `requirements.txt`** : Termasuk Locust dan dependensi lainnya.

## Instalasi

Ikuti langkah-langkah berikut untuk mengatur lingkungan dan menjalankan pengujian:

### Kloning Repository

```bash
git clone https://github.com/gendonholaholo/Locust.git
cd Locust
```

### Membuat Virtual Environment

```bash
python -m venv venv
```

### Aktifkan Virtual Environment
Windows

```bash
venv\\Scripts\\activate
```

macOS/Linux

```bash
source venv/bin/activate
```

### Insatallasi Depedensi

```bash
pip install -r requirements.txt
```

### Menjalankan Pengujian
Setelah instalasi selesai, Anda dapat menjalankan pengujian beban dengan Locust.

Menjalankan Locust
```bash
locust -f locustfile.py
```

Perintah ini akan memulai antarmuka web Locust yang dapat diakses melalui http://localhost:8089.

### Mengonfigurasi Pengujian
Di antarmuka web Locust:

- Number of total users to simulate : Masukkan jumlah pengguna yang ingin disimulasikan.
- Spawn rate : Tentukan berapa banyak pengguna yang ditambahkan per detik.
- Host : URL dari aplikasi yang akan diuji.
  
Setelah mengisi parameter tersebut, klik Start Swarming untuk memulai pengujian.

### Melihat Laporan Pengujian
Setelah pengujian selesai, Locust akan menampilkan statistik kinerja di antarmuka web. Untuk menyimpan laporan dalam bentuk file, Anda dapat mengonfigurasi Locust untuk menghasilkan laporan dalam format CSV atau HTML dan menyimpannya di direktori reports/.

### Catatan Tambahan
Kustomisasi Pengujian : Anda dapat memodifikasi locustfile.py dan menambahkan skrip tambahan di direktori tests/ untuk menyesuaikan skenario pengujian sesuai kebutuhan.
Konfigurasi Tambahan : Sesuaikan file di direktori config/ untuk mengatur parameter pengujian lainnya, seperti waktu tunggu, header HTTP, atau data autentikasi.
Untuk informasi lebih lanjut tentang penggunaan dan kustomisasi Locust, kunjungi dokumentasi resmi di: https://locust.io/.
