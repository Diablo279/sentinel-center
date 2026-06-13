# INSTALLATION.md - Panduan Instalasi Cepat

## 🚀 Quick Installation (Recommended)

### 1. Jalankan Setup Script
```bash
bash setup.sh
```

Setup script akan:
- ✅ Check versi Python
- ✅ Install dependencies (psutil)
- ✅ Check nmap installation
- ✅ Setup file permissions

### 2. Mulai Aplikasi
```bash
python3 main.py
```

---

## 📋 Manual Installation

Jika ingin install secara manual:

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Install nmap (Optional)

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
- Download dari: https://nmap.org/download.html
- Atau gunakan Chocolatey: `choco install nmap`

### 3. Verify Installation
```bash
# Test Python modules
python3 -c "import psutil; print('psutil OK')"

# Test nmap (if installed)
nmap --version
```

### 4. Run Application
```bash
python3 main.py
```

---

## 🔧 Troubleshooting Installation

### Error: "pip: command not found"
```bash
# Install pip for Python 3
sudo apt install python3-pip
```

### Error: "ModuleNotFoundError: No module named 'psutil'"
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Error: "nmap: command not found" (Network Scanner)
- Aplikasi tetap bisa dijalankan tanpa nmap
- Network Scanner akan menampilkan pesan error
- Install nmap jika ingin menggunakan fitur ini

### Permission Denied saat File Scanning
- Program akan skip folder yang tidak accessible
- Atau jalankan dengan: `sudo python3 main.py` (not recommended)

---

## ✅ Installation Checklist

- [ ] Python 3.7+ installed
- [ ] pip installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] nmap installed (optional)
- [ ] main.py executable (`chmod +x main.py`)
- [ ] Can run application without errors

---

## 📞 Need Help?

1. Check [DOCUMENTATION.md](DOCUMENTATION.md) for detailed docs
2. Check Python version: `python3 --version`
3. Check pip packages: `pip list | grep psutil`
4. Check nmap: `nmap --version`

---

**Last Updated:** 2026-06-13
