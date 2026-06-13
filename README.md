# 🛡️ Sentinel Control Center

Aplikasi CLI modular untuk monitoring sistem, scanning file, dan network discovery.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
sudo apt install nmap  # (optional, untuk network scanner)
```

### 2. Jalankan Aplikasi
```bash
python3 main.py
```

## 📦 Modul-Modul

| Modul | Fungsi | Library |
|-------|--------|---------|
| **Monitor** | RAM & HDD Usage | psutil |
| **Scanner** | Junk Files & Old Files | Built-in |
| **Net Tool** | Network Scanning | nmap |

## 📁 Struktur Project

```
sentinel-center/
├── main.py               # Entry point CLI
├── requirements.txt      # Python dependencies
├── DOCUMENTATION.md      # Full documentation
├── README.md            # This file
└── sentinel/
    ├── __init__.py
    ├── monitor.py       # Monitor modul
    ├── scanner.py       # Scanner modul
    └── net_tool.py      # Network tool modul
```

## 📖 Dokumentasi Lengkap

Lihat [DOCUMENTATION.md](DOCUMENTATION.md) untuk penjelasan detail tentang:
- Instalasi lengkap
- Cara penggunaan setiap modul
- Konfigurasi dan customization
- Troubleshooting

## ✨ Fitur Utama

✅ **Monitor System**
- Real-time RAM usage monitoring
- HDD/SSD usage per partition
- Visual progress bars
- Auto-formatting untuk bytes

✅ **File Scanner**
- Cari .tmp dan .log files
- Cari .py/.go files tidak diakses > 90 hari
- Display file size dan location
- Hanya list, tidak hapus!

✅ **Network Scanner**
- Host discovery di local network
- Port scanning untuk IP tertentu
- Quick scan & advanced mode
- Hostname resolution

## 🔧 Requirements

- Python 3.7+
- psutil >= 5.9.0
- nmap (optional, untuk network scanner)

## 💡 Usage Examples

### Monitor RAM
```bash
python3 main.py
# Choose: 1 → 1 (Monitor RAM Usage)
```

### Scan Junk Files
```bash
python3 main.py
# Choose: 2 → 1 (Scan Junk Files)
```

### Quick Network Scan
```bash
python3 main.py
# Choose: 3 → 1 (Quick Scan)
```

## 🐛 Troubleshooting

**psutil not found?**
```bash
pip install psutil
```

**nmap not found?**
```bash
sudo apt install nmap
```

Lihat [DOCUMENTATION.md](DOCUMENTATION.md) untuk troubleshooting lengkap.

## 📝 Notes

- ✅ Monitor & Scanner hanya READ-ONLY, tidak modifikasi sistem
- ✅ Network scanning untuk authorized networks saja
- ⏱️ Scanning besar mungkin butuh waktu beberapa menit

## 📄 Version

**Sentinel Control Center v1.0**
Created: 2026-06-13
