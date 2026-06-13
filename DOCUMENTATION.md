# Sentinel Control Center - Dokumentasi

## 📋 Daftar Isi
- [Tentang Aplikasi](#tentang-aplikasi)
- [Struktur Proyek](#struktur-proyek)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Modul-Modul](#modul-modul)
- [Troubleshooting](#troubleshooting)

---

## 🛡️ Tentang Aplikasi

**Sentinel Control Center** adalah aplikasi berbasis CLI (Command Line Interface) yang dirancang untuk:
- 📊 Memantau penggunaan sistem (RAM & HDD)
- 🔍 Memindai file sampah dan file yang tidak diakses
- 🌐 Network scanning dan port discovery

Aplikasi ini dibangun dengan arsitektur modular, memudahkan untuk maintenance dan extension.

---

## 📁 Struktur Proyek

```
sentinel-center/
├── main.py                 # Script utama dengan CLI menu
├── requirements.txt        # Dependency Python
├── DOCUMENTATION.md        # File dokumentasi ini
├── README.md              # Penjelasan singkat
└── sentinel/
    ├── __init__.py        # Package initialization
    ├── monitor.py         # Modul monitoring RAM & HDD
    ├── scanner.py         # Modul file scanning
    └── net_tool.py        # Modul network scanning
```

---

## 🚀 Instalasi

### Prasyarat
- Python 3.7 atau lebih baru
- pip (package manager untuk Python)
- nmap (untuk fitur network scanning - optional)

### Langkah-Langkah Instalasi

#### 1. Install Dependencies Python

```bash
# Masuk ke direktori proyek
cd sentinel-center

# Install dependencies dari requirements.txt
pip install -r requirements.txt
```

#### 2. Install nmap (Optional, untuk Network Scanner)

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install nmap
```

**CentOS/RHEL:**
```bash
sudo yum install nmap
```

**macOS:**
```bash
brew install nmap
```

**Windows:**
Download dari: https://nmap.org/download.html

#### 3. Verifikasi Instalasi

```bash
# Test psutil
python3 -c "import psutil; print('psutil OK')"

# Test nmap (jika sudah diinstall)
nmap --version
```

---

## 💻 Penggunaan

### Menjalankan Aplikasi

```bash
# Dari direktori sentinel-center
python3 main.py
```

### Menu Utama

Setelah menjalankan aplikasi, Anda akan melihat menu utama:

```
🛡️  SENTINEL CONTROL CENTER 🛡️

📋 MAIN MENU
================================================================================

  1. 📊 Monitor System (RAM & HDD Usage)
  2. 🔍 File Scanner (Junk Files & Old Files)
  3. 🌐 Network Scanner
  4. ℹ️  Informasi Aplikasi
  5. ❌ Keluar

================================================================================
```

Ketik nomor pilihan Anda dan tekan Enter.

---

## 🔧 Modul-Modul

### 1. Monitor Module (`monitor.py`)

**Fungsi:** Memantau penggunaan RAM dan HDD/SSD secara real-time

**Fitur:**
- ✅ Menampilkan total RAM dan penggunaan saat ini
- ✅ Visualisasi penggunaan dalam bentuk progress bar
- ✅ Informasi untuk setiap partisi disk
- ✅ Persentase penggunaan dan ruang tersedia

**Cara Kerja:**
- Menggunakan library `psutil` untuk mengakses data sistem
- Menampilkan data dalam format yang mudah dibaca
- Auto-formatting untuk bytes ke KB/MB/GB

**Contoh Output:**
```
📊 MONITOR PENGGUNAAN RAM
============================================================
Total RAM          : 16.00 GB
RAM Terpakai       : 8.45 GB
RAM Tersedia       : 7.55 GB
Penggunaan         : 52.8%
Progress           : [████████████████░░░░░░░░░░░░░░░░░░]
============================================================
```

---

### 2. Scanner Module (`scanner.py`)

**Fungsi:** Memindai file sampah dan file yang tidak diakses dalam jangka panjang

**Fitur:**
- ✅ Mencari file temporary (`.tmp`)
- ✅ Mencari log files (`.log`)
- ✅ Mencari file `.py` dan `.go` yang tidak diakses > 90 hari
- ✅ Menampilkan ukuran file dan lokasi
- ✅ **PENTING:** Hanya menampilkan daftar, TIDAK menghapus file

**Cara Kerja:**
- Menggunakan `os.walk()` untuk traverse direktori
- Mengecek waktu akses terakhir file (access time)
- Skip folder umum yang tidak penting (.git, __pycache__, node_modules, .venv)
- Sort hasil berdasarkan umur file

**Contoh Output:**
```
🗑️  SCAN FILE SAMPAH (.tmp dan .log)
================================================================================

📊 Total file sampah ditemukan: 15
📈 Total ukuran: 2.45 MB

No.  Tipe   Ukuran       Path
────────────────────────────────────────────────────────────────────────────
1    .tmp   256.50 KB    /home/user/.cache/file1.tmp
2    .log   1.20 MB      /home/user/logs/app.log
```

---

### 3. Net Tool Module (`net_tool.py`)

**Fungsi:** Network scanning dan port discovery menggunakan nmap

**Fitur:**
- ✅ Host discovery di jaringan lokal
- ✅ Port scanning pada IP tertentu
- ✅ Quick scan mode (default: 192.168.1.0/24)
- ✅ Advanced scan mode (custom range)
- ✅ Deteksi hostname dari IP address

**Cara Kerja:**
- Menggunakan command-line `nmap` untuk scanning
- Parse output nmap menggunakan regex
- Timeout protection untuk scanning yang terlalu lama
- Auto-check untuk nmap installation

**Persyaratan:**
- nmap harus sudah terinstall di sistem
- Network access ke target network (mungkin butuh sudo)

**Catatan Keamanan:**
- Network scanning harus dilakukan dengan izin
- Jangan scan network yang bukan milik Anda
- Beberapa network mungkin memblokir nmap traffic

**Contoh Output:**
```
🌐 NETWORK SCANNER
================================================================================

📍 Local IP: 192.168.1.100
🔍 Target Network: 192.168.1.0/24

📊 Total host aktif ditemukan: 8

No.  IP Address      Hostname              Status
────────────────────────────────────────────────────────────
1    192.168.1.1     gateway.local         Up
2    192.168.1.100   mycomputer            Up
3    192.168.1.105   printer.local         Up
```

---

## ⚙️ Konfigurasi

### Mengubah Threshold File Lama

Edit `scanner.py`, ubah nilai `days` di fungsi `find_old_files()`:

```python
old_files = find_old_files(days=180)  # 180 hari instead of 90
```

### Mengubah Network Range Default

Edit `net_tool.py`, ubah value di fungsi `scan_quick()`:

```python
display_scan_results("10.0.0.0/24")  # Ganti dengan range Anda
```

### Mengubah Jumlah Port yang Di-scan

Edit `net_tool.py`, ubah parameter `top_ports`:

```python
open_ports = scan_ports(ip_address, top_ports=50)  # Scan 50 port instead of 20
```

---

## 🐛 Troubleshooting

### Masalah: `ModuleNotFoundError: No module named 'psutil'`

**Solusi:**
```bash
pip install psutil
```

### Masalah: `nmap: command not found`

**Solusi:**
```bash
# Ubuntu/Debian
sudo apt install nmap

# macOS
brew install nmap
```

### Masalah: Permission Denied saat scanning file

**Penyebab:** Program tidak memiliki permission untuk akses beberapa direktori

**Solusi:**
- Jalankan dengan `sudo` (tidak disarankan)
- Atau scan hanya direktori yang accessible
- Program akan otomatis skip direktori yang tidak accessible

### Masalah: Network scan timeout

**Penyebab:** Network terlalu besar atau nmap terlalu lambat

**Solusi:**
- Gunakan network range yang lebih kecil
- Contoh: `192.168.1.0/25` instead of `192.168.0.0/16`
- Atau gunakan port scan untuk IP tertentu saja

### Masalah: Performa lambat saat scanning file

**Penyebab:** Banyak file untuk di-scan di home directory

**Solusi:**
- Edit `scanner.py` dan ubah `search_path` ke folder spesifik
- Atau menambah folder ke skip list
- Contoh:
```python
dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', 'node_modules', '.venv', '.cache']]
```

---

## 📝 Catatan Penting

### Keamanan
- ✅ Monitor module hanya membaca informasi, tidak menulis
- ✅ Scanner module hanya menampilkan daftar, tidak menghapus file
- ✅ Net tool module hanya read-only, tidak modifikasi network

### Kompatibilitas
- ✅ Teruji di Ubuntu 20.04+, Debian 10+
- ✅ Kompatibel dengan macOS 10.15+
- ⚠️ Di Windows, beberapa fitur mungkin terbatas (gunakan WSL untuk hasil terbaik)

### Performance
- Monitor module: Response time < 1 detik
- Scanner module: Tergantung ukuran directory (bisa 30 detik - 5 menit)
- Net tool module: Tergantung ukuran network (bisa 1 - 10 menit)

---

## 🆘 Support & Feedback

Jika mengalami masalah atau memiliki saran:
1. Cek bagian Troubleshooting di atas
2. Verifikasi semua dependencies terinstall dengan benar
3. Coba jalankan test sederhana untuk setiap modul

---

## 📜 Lisensi

Sentinel Control Center v1.0
Dibuat untuk system monitoring dan management purposes

---

**Last Updated:** 2026-06-13
