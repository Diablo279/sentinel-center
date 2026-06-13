"""
Scanner Module - Memindai file sampah dan file yang tidak diakses lama
Mencari file dengan ekstensi .tmp, .log, serta file .py/.go yang tidak diakses > 90 hari
"""

import os
import glob
from datetime import datetime, timedelta
from pathlib import Path


def find_temp_files(search_path=None):
    """
    Mencari file temporary (.tmp) di sistem
    
    Args:
        search_path (str): Path untuk pencarian (default: home directory)
        
    Returns:
        list: List berisi path file .tmp yang ditemukan
    """
    if search_path is None:
        search_path = os.path.expanduser("~")
    
    temp_files = []
    
    try:
        # Cari file dengan ekstensi .tmp
        for root, dirs, files in os.walk(search_path):
            # Skip beberapa folder yang tidak penting
            dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', 'node_modules', '.venv']]
            
            for file in files:
                if file.endswith('.tmp'):
                    full_path = os.path.join(root, file)
                    try:
                        file_size = os.path.getsize(full_path)
                        temp_files.append({
                            'path': full_path,
                            'size': file_size,
                            'type': '.tmp'
                        })
                    except (OSError, PermissionError):
                        pass
    except PermissionError:
        pass
    
    return temp_files


def find_log_files(search_path=None):
    """
    Mencari file log (.log) di sistem
    
    Args:
        search_path (str): Path untuk pencarian (default: home directory)
        
    Returns:
        list: List berisi path file .log yang ditemukan
    """
    if search_path is None:
        search_path = os.path.expanduser("~")
    
    log_files = []
    
    try:
        for root, dirs, files in os.walk(search_path):
            # Skip beberapa folder yang tidak penting
            dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', 'node_modules', '.venv']]
            
            for file in files:
                if file.endswith('.log'):
                    full_path = os.path.join(root, file)
                    try:
                        file_size = os.path.getsize(full_path)
                        log_files.append({
                            'path': full_path,
                            'size': file_size,
                            'type': '.log'
                        })
                    except (OSError, PermissionError):
                        pass
    except PermissionError:
        pass
    
    return log_files


def find_old_files(search_path=None, days=90, extensions=['.py', '.go']):
    """
    Mencari file yang tidak diakses lebih dari N hari
    
    Args:
        search_path (str): Path untuk pencarian (default: home directory)
        days (int): Jumlah hari sebagai threshold (default: 90)
        extensions (list): Ekstensi file yang dicari (default: ['.py', '.go'])
        
    Returns:
        list: List berisi file yang tidak diakses lebih dari N hari
    """
    if search_path is None:
        search_path = os.path.expanduser("~")
    
    old_files = []
    cutoff_time = datetime.now() - timedelta(days=days)
    
    try:
        for root, dirs, files in os.walk(search_path):
            # Skip beberapa folder yang tidak penting
            dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', 'node_modules', '.venv']]
            
            for file in files:
                # Cek apakah file memiliki ekstensi yang dicari
                if any(file.endswith(ext) for ext in extensions):
                    full_path = os.path.join(root, file)
                    
                    try:
                        # Dapatkan waktu akses terakhir
                        access_time = datetime.fromtimestamp(os.path.getatime(full_path))
                        
                        if access_time < cutoff_time:
                            file_size = os.path.getsize(full_path)
                            old_files.append({
                                'path': full_path,
                                'last_access': access_time,
                                'size': file_size,
                                'type': Path(file).suffix,
                                'days_old': (datetime.now() - access_time).days
                            })
                    except (OSError, PermissionError):
                        pass
    except PermissionError:
        pass
    
    # Sort berdasarkan waktu akses (yang paling lama di atas)
    old_files.sort(key=lambda x: x['last_access'])
    
    return old_files


def format_bytes(bytes_value):
    """
    Mengkonversi bytes ke format yang lebih readable
    
    Args:
        bytes_value (int): Nilai dalam bytes
        
    Returns:
        str: String terformat dengan unit
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.2f} {unit}"
        bytes_value /= 1024.0
    
    return f"{bytes_value:.2f} TB"


def display_junk_files():
    """
    Menampilkan daftar file sampah (.tmp dan .log)
    """
    print("\n" + "="*80)
    print("🗑️  SCAN FILE SAMPAH (.tmp dan .log)")
    print("="*80)
    
    temp_files = find_temp_files()
    log_files = find_log_files()
    
    all_junk = temp_files + log_files
    
    if not all_junk:
        print("\n✅ Tidak ada file sampah yang ditemukan\n")
        print("="*80 + "\n")
        return
    
    print(f"\n📊 Total file sampah ditemukan: {len(all_junk)}")
    
    total_size = sum(f['size'] for f in all_junk)
    print(f"📈 Total ukuran: {format_bytes(total_size)}\n")
    
    print(f"{'No.':<4} {'Tipe':<6} {'Ukuran':<12} {'Path':<58}")
    print("-"*80)
    
    for i, file in enumerate(all_junk, 1):
        file_type = file['type']
        file_size = format_bytes(file['size'])
        path = file['path']
        
        # Potong path jika terlalu panjang
        if len(path) > 57:
            path = "..." + path[-54:]
        
        print(f"{i:<4} {file_type:<6} {file_size:<12} {path:<58}")
    
    print("="*80 + "\n")


def display_old_files():
    """
    Menampilkan daftar file .py dan .go yang tidak diakses > 90 hari
    """
    print("\n" + "="*100)
    print("⏳ SCAN FILE LAMA (tidak diakses > 90 hari)")
    print("="*100)
    
    old_files = find_old_files(days=90, extensions=['.py', '.go'])
    
    if not old_files:
        print("\n✅ Tidak ada file lama yang ditemukan\n")
        print("="*100 + "\n")
        return
    
    print(f"\n📊 Total file lama ditemukan: {len(old_files)}")
    
    total_size = sum(f['size'] for f in old_files)
    print(f"📈 Total ukuran: {format_bytes(total_size)}\n")
    
    print(f"{'No.':<4} {'Tipe':<5} {'Umur (hari)':<12} {'Ukuran':<12} {'Path':<60}")
    print("-"*100)
    
    for i, file in enumerate(old_files, 1):
        file_type = file['type']
        days_old = file['days_old']
        file_size = format_bytes(file['size'])
        path = file['path']
        
        # Potong path jika terlalu panjang
        if len(path) > 59:
            path = "..." + path[-56:]
        
        print(f"{i:<4} {file_type:<5} {days_old:<12} {file_size:<12} {path:<60}")
    
    print("="*100 + "\n")


def scan_all():
    """
    Menjalankan semua scan (file sampah dan file lama)
    """
    print("\n" + "🔍 Memulai proses scanning...")
    print("   (Ini mungkin memakan waktu beberapa saat)\n")
    
    display_junk_files()
    display_old_files()
    
    print("✅ Scan selesai!\n")


if __name__ == "__main__":
    scan_all()
