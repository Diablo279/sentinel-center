"""
Monitor Module - Memantau penggunaan RAM dan HDD
Menggunakan library psutil untuk mendapatkan informasi sistem
"""

import psutil
from datetime import datetime


def get_memory_info():
    """
    Fungsi untuk mendapatkan informasi penggunaan RAM
    
    Returns:
        dict: Informasi RAM dengan detail total, used, available, percent
    """
    memory = psutil.virtual_memory()
    
    info = {
        'total': memory.total,
        'used': memory.used,
        'available': memory.available,
        'percent': memory.percent,
        'free': memory.free
    }
    
    return info


def get_disk_info():
    """
    Fungsi untuk mendapatkan informasi penggunaan HDD/SSD
    
    Returns:
        list: List berisi informasi untuk setiap partisi disk
    """
    disk_info = []
    
    try:
        partitions = psutil.disk_partitions()
        
        for partition in partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                
                disk_info.append({
                    'device': partition.device,
                    'mountpoint': partition.mountpoint,
                    'fstype': partition.fstype,
                    'total': usage.total,
                    'used': usage.used,
                    'free': usage.free,
                    'percent': usage.percent
                })
            except PermissionError:
                # Skip partisi yang tidak bisa diakses
                continue
    
    except Exception as e:
        print(f"Error mendapatkan informasi disk: {e}")
    
    return disk_info


def format_bytes(bytes_value):
    """
    Fungsi untuk mengkonversi bytes ke format yang lebih readable
    
    Args:
        bytes_value (int): Nilai dalam bytes
        
    Returns:
        str: String terformat dengan unit (B, KB, MB, GB, TB)
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.2f} {unit}"
        bytes_value /= 1024.0
    
    return f"{bytes_value:.2f} PB"


def display_memory_info():
    """
    Menampilkan informasi penggunaan RAM dalam format yang rapi
    """
    print("\n" + "="*60)
    print("📊 MONITOR PENGGUNAAN RAM")
    print("="*60)
    
    memory = get_memory_info()
    
    print(f"Total RAM          : {format_bytes(memory['total'])}")
    print(f"RAM Terpakai       : {format_bytes(memory['used'])}")
    print(f"RAM Tersedia       : {format_bytes(memory['available'])}")
    print(f"Penggunaan         : {memory['percent']}%")
    
    # Visualisasi progress bar
    bar_length = 40
    filled = int(bar_length * memory['percent'] / 100)
    bar = '█' * filled + '░' * (bar_length - filled)
    print(f"Progress           : [{bar}]")
    
    print("="*60 + "\n")


def display_disk_info():
    """
    Menampilkan informasi penggunaan HDD/SSD dalam format yang rapi
    """
    print("\n" + "="*60)
    print("💾 MONITOR PENGGUNAAN DISK/HDD")
    print("="*60)
    
    disks = get_disk_info()
    
    if not disks:
        print("⚠️  Tidak ada informasi disk yang dapat ditampilkan")
        print("="*60 + "\n")
        return
    
    for i, disk in enumerate(disks, 1):
        print(f"\nDisk {i}: {disk['device']}")
        print(f"  Mount Point    : {disk['mountpoint']}")
        print(f"  File System    : {disk['fstype']}")
        print(f"  Total          : {format_bytes(disk['total'])}")
        print(f"  Terpakai       : {format_bytes(disk['used'])}")
        print(f"  Tersedia       : {format_bytes(disk['free'])}")
        print(f"  Penggunaan     : {disk['percent']}%")
        
        # Visualisasi progress bar
        bar_length = 30
        filled = int(bar_length * disk['percent'] / 100)
        bar = '█' * filled + '░' * (bar_length - filled)
        print(f"  Progress       : [{bar}]")
    
    print("\n" + "="*60 + "\n")


def monitor_all():
    """
    Menampilkan semua informasi monitoring (RAM dan Disk)
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n⏰ Last Update: {timestamp}")
    
    display_memory_info()
    display_disk_info()


if __name__ == "__main__":
    monitor_all()
