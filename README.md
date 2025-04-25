# Scraping Terjadwal Properti Bukit Vista Menggunakan Github Action

🎯 Objective
Membangun pipeline otomatis untuk melakukan web scraping data properti dari situs Bukit Vista, memproses data tersebut, dan mengunggah hasilnya ke Google Drive. Proyek ini bertujuan untuk mengambil data terkini secara efisien tanpa intervensi manual, dengan memanfaatkan GitHub Actions untuk penjadwalan otomatis dan integrasi dengan Google Drive untuk penyimpanan hasil.

## ⚙️ Fitur Utama
- **Web Scraping Otomatis**: Mengambil data properti dari situs Bukit Vista.
- **Pemrosesan Data**: Menyimpan data dalam format Excel dengan penamaan berdasarkan tanggal.
- **Integrasi Google Drive**: Mengunggah file hasil scraping ke folder tertentu di Google Drive.
- **Penjadwalan dengan GitHub Actions**: Menjalankan proses secara otomatis setiap hari pada pukul 17:30 WIB.

## 🗂️ Struktur Proyek
. ├── scraping.py # Script untuk melakukan web scraping ├── upload_to_drive.py # Script untuk mengunggah file ke Google Drive ├── requirements.txt # Daftar dependensi Python ├── .github/ │ └── workflows/ │ └── main.yml # Workflow GitHub Actions untuk penjadwalan otomatis └── README.md # Dokumentasi proyek


📁 Hasil
File hasil scraping akan disimpan dalam format Excel dengan nama:

data_bukit_vista_<tanggal>.xlsx

property_description_<tanggal>.xlsx

File-file ini akan diunggah ke folder Google Drive yang telah ditentukan oleh FOLDER_ID dalam script upload_to_drive.py.
