"""
Sentinel Control Center - Aplikasi Utama
Menu CLI untuk menjalankan ketiga modul: Monitor, Scanner, dan Net Tool
"""

import sys
import os
from datetime import datetime

# Tambahkan path sentinel folder ke sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sentinel'))

# Import modul-modul
from sentinel import monitor, scanner, net_tool


def display_header():
    """
    Menampilkan header aplikasi
    """
    print("\n" + "="*80)
    print(" " * 20 + "🛡️  SENTINEL CONTROL CENTER 🛡️")
    print("="*80)
    print("   Aplikasi untuk monitoring, scanning, dan network discovery")
    print("="*80 + "\n")


def display_menu():
    """
    Menampilkan menu utama
    """
    print("\n" + "="*80)
    print("📋 MAIN MENU")
    print("="*80)
    print("\n  1. 📊 Monitor System (RAM & HDD Usage)")
    print("  2. 🔍 File Scanner (Junk Files & Old Files)")
    print("  3. 🌐 Network Scanner")
    print("  4. ℹ️  Informasi Aplikasi")
    print("  5. ❌ Keluar\n")
    print("="*80)


def display_info():
    """
    Menampilkan informasi tentang aplikasi
    """
    print("\n" + "="*80)
    print("ℹ️  INFORMASI SENTINEL CONTROL CENTER")
    print("="*80)
    
    info_text = """
📌 TENTANG APLIKASI:
   Sentinel Control Center adalah aplikasi CLI yang dirancang untuk memantau
   dan mengelola sistem komputer dengan tiga modul utama:

🔧 MODUL-MODUL:

   1️⃣  MONITOR MODULE
       Fungsi: Memantau penggunaan RAM dan HDD/SSD
       Library: psutil
       Fitur:
       • Menampilkan total RAM dan penggunaan real-time
       • Visualisasi penggunaan dalam bentuk progress bar
       • Informasi disk untuk setiap partisi
       • Persentase penggunaan disk

   2️⃣  SCANNER MODULE
       Fungsi: Memindai file sampah dan file yang tidak diakses lama
       Fitur:
       • Mencari file temporary (.tmp)
       • Mencari log files (.log)
       • Mencari file .py dan .go yang tidak diakses > 90 hari
       • Menampilkan ukuran dan lokasi file
       • CATATAN: Hanya menampilkan daftar, tidak menghapus file

   3️⃣  NET TOOL MODULE
       Fungsi: Network scanning dan port discovery
       Library: nmap (harus diinstall terpisah)
       Fitur:
       • Host discovery di jaringan lokal
       • Port scanning pada IP tertentu
       • Quick scan mode (192.168.1.0/24)
       • Advanced scan mode (custom network range)

💡 CARA PENGGUNAAN:
   • Gunakan nomor menu untuk memilih modul
   • Setiap modul akan menampilkan hasil dalam format yang mudah dibaca
   • Tekan Enter untuk kembali ke menu utama setelah setiap operasi

⚙️  REQUIREMENTS:
   • Python 3.7+
   • psutil (untuk Monitor Module)
   • nmap (untuk Net Tool Module) - install dengan: sudo apt install nmap

👨‍💻 DEVELOPER:
   Sentinel Control Center v1.0
"""
    
    print(info_text)
    print("="*80 + "\n")


def show_loading():
    """
    Menampilkan animasi loading
    """
    print("\n⏳ Processing", end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
        import time
        time.sleep(0.3)
    print(" Done!\n")


def handle_monitor_menu():
    """
    Handle menu Monitor System
    """
    print("\n" + "="*80)
    print("📊 MONITOR SYSTEM MENU")
    print("="*80)
    print("\n  1. Monitor RAM Usage")
    print("  2. Monitor Disk Usage")
    print("  3. Monitor All (RAM + Disk)")
    print("  4. Kembali ke Menu Utama\n")
    print("="*80)
    
    choice = input("\nPilih opsi (1-4): ").strip()
    
    if choice == '1':
        print("\n🔄 Mengambil informasi RAM...")
        monitor.display_memory_info()
    
    elif choice == '2':
        print("\n🔄 Mengambil informasi Disk...")
        monitor.display_disk_info()
    
    elif choice == '3':
        print("\n🔄 Mengambil informasi System...")
        monitor.monitor_all()
    
    elif choice == '4':
        return
    
    else:
        print("\n❌ Opsi tidak valid. Silakan coba lagi.")
        handle_monitor_menu()


def handle_scanner_menu():
    """
    Handle menu File Scanner
    """
    print("\n" + "="*80)
    print("🔍 FILE SCANNER MENU")
    print("="*80)
    print("\n  1. Scan File Sampah (.tmp & .log)")
    print("  2. Scan File Lama (tidak diakses > 90 hari)")
    print("  3. Scan Semua")
    print("  4. Kembali ke Menu Utama\n")
    print("="*80)
    
    choice = input("\nPilih opsi (1-4): ").strip()
    
    if choice == '1':
        print("\n🔄 Scanning file sampah...")
        scanner.display_junk_files()
    
    elif choice == '2':
        print("\n🔄 Scanning file lama...")
        scanner.display_old_files()
    
    elif choice == '3':
        print("\n🔄 Scanning semua file...")
        scanner.scan_all()
    
    elif choice == '4':
        return
    
    else:
        print("\n❌ Opsi tidak valid. Silakan coba lagi.")
        handle_scanner_menu()


def handle_nettools_menu():
    """
    Handle menu Network Scanner
    """
    print("\n" + "="*80)
    print("🌐 NETWORK SCANNER MENU")
    print("="*80)
    print("\n  1. Quick Scan (Default: 192.168.1.0/24)")
    print("  2. Advanced Scan (Custom Network/Port)")
    print("  3. Kembali ke Menu Utama\n")
    print("="*80)
    
    choice = input("\nPilih opsi (1-3): ").strip()
    
    if choice == '1':
        net_tool.scan_quick()
    
    elif choice == '2':
        net_tool.scan_advanced()
    
    elif choice == '3':
        return
    
    else:
        print("\n❌ Opsi tidak valid. Silakan coba lagi.")
        handle_nettools_menu()


def main():
    """
    Fungsi utama - loop menu utama
    """
    display_header()
    
    while True:
        display_menu()
        
        choice = input("Pilih opsi (1-5): ").strip()
        
        if choice == '1':
            handle_monitor_menu()
        
        elif choice == '2':
            handle_scanner_menu()
        
        elif choice == '3':
            handle_nettools_menu()
        
        elif choice == '4':
            display_info()
        
        elif choice == '5':
            print("\n" + "="*80)
            print("👋 Terima kasih telah menggunakan Sentinel Control Center!")
            print("   Sampai jumpa lagi!")
            print("="*80 + "\n")
            sys.exit(0)
        
        else:
            print("\n❌ Opsi tidak valid. Silakan pilih 1-5.")
        
        # Prompt untuk kembali ke menu
        if choice in ['1', '2', '3', '4']:
            input("\nTekan Enter untuk kembali ke menu utama...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Program dihentikan oleh user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error tidak terduga: {e}")
        sys.exit(1)
