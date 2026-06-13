"""
Net Tool Module - Memindai jaringan lokal menggunakan Nmap
Module ini menyediakan fungsi untuk scanning host dan port di jaringan lokal
"""

import subprocess
import re
from datetime import datetime


def check_nmap_installed():
    """
    Cek apakah nmap sudah terinstall di sistem
    
    Returns:
        bool: True jika nmap terinstall, False jika tidak
    """
    try:
        subprocess.run(['nmap', '--version'], 
                      capture_output=True, 
                      timeout=5,
                      check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        return False


def get_local_network():
    """
    Mendapatkan IP lokal dan range jaringan
    
    Returns:
        dict: Informasi IP lokal dan subnet mask
    """
    try:
        result = subprocess.run(['hostname', '-I'], 
                               capture_output=True, 
                               text=True,
                               timeout=5)
        
        ip_addresses = result.stdout.strip().split()
        
        if ip_addresses:
            return {
                'local_ip': ip_addresses[0],
                'all_ips': ip_addresses
            }
    except Exception:
        pass
    
    return None


def scan_network(network_range):
    """
    Melakukan network scan menggunakan nmap untuk menemukan host aktif
    
    Args:
        network_range (str): Range jaringan (contoh: 192.168.1.0/24)
        
    Returns:
        list: List berisi informasi host yang ditemukan
    """
    if not check_nmap_installed():
        print("❌ Nmap tidak terinstall!")
        print("   Install nmap dengan command: sudo apt install nmap")
        return []
    
    hosts = []
    
    try:
        # Gunakan nmap untuk scan network dengan opsi -sn (ping scan)
        print(f"⏳ Scanning network {network_range}...")
        
        result = subprocess.run(
            ['nmap', '-sn', network_range],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        # Parse output nmap
        lines = result.stdout.split('\n')
        
        for line in lines:
            # Cari pattern "Nmap scan report for <IP> (<Hostname>)"
            match = re.search(r'Nmap scan report for (.+?)(\s*\((.+?)\))?$', line)
            
            if match:
                ip = match.group(1).strip()
                hostname = match.group(3) if match.group(3) else "Unknown"
                
                hosts.append({
                    'ip': ip,
                    'hostname': hostname,
                    'status': 'Up'
                })
        
    except subprocess.TimeoutExpired:
        print("⚠️  Scan timeout - jaringan mungkin terlalu besar")
    except FileNotFoundError:
        print("❌ Nmap tidak ditemukan di PATH")
    except Exception as e:
        print(f"❌ Error saat scanning: {e}")
    
    return hosts


def scan_ports(ip_address, top_ports=20):
    """
    Melakukan port scan pada IP tertentu
    
    Args:
        ip_address (str): IP address untuk di-scan
        top_ports (int): Jumlah port populer yang di-scan (default: 20)
        
    Returns:
        list: List berisi informasi port yang terbuka
    """
    if not check_nmap_installed():
        print("❌ Nmap tidak terinstall!")
        return []
    
    open_ports = []
    
    try:
        print(f"⏳ Scanning port pada {ip_address}...")
        
        # Gunakan nmap untuk scan port dengan opsi --top-ports
        result = subprocess.run(
            ['nmap', '--top-ports', str(top_ports), ip_address],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        # Parse output nmap untuk mencari port yang terbuka
        lines = result.stdout.split('\n')
        
        for line in lines:
            # Cari pattern "PORT STATE SERVICE"
            match = re.search(r'^(\d+)/(\w+)\s+(\w+)', line)
            
            if match:
                port = match.group(1)
                protocol = match.group(2)
                state = match.group(3)
                
                if state == 'open':
                    open_ports.append({
                        'port': port,
                        'protocol': protocol,
                        'state': state
                    })
    
    except subprocess.TimeoutExpired:
        print(f"⚠️  Scan port timeout untuk {ip_address}")
    except Exception as e:
        print(f"❌ Error saat scanning port: {e}")
    
    return open_ports


def display_scan_results(network_range):
    """
    Menampilkan hasil network scan dalam format yang rapi
    
    Args:
        network_range (str): Range jaringan untuk di-scan
    """
    print("\n" + "="*80)
    print("🌐 NETWORK SCANNER")
    print("="*80)
    
    # Cek nmap
    if not check_nmap_installed():
        print("\n❌ NMAP TIDAK TERINSTALL")
        print("\nUntuk menggunakan fitur network scanning, silakan install nmap:")
        print("   Ubuntu/Debian: sudo apt install nmap")
        print("   CentOS/RHEL:   sudo yum install nmap")
        print("   macOS:         brew install nmap")
        print("="*80 + "\n")
        return
    
    # Dapatkan info jaringan lokal
    local_net = get_local_network()
    
    if local_net:
        print(f"\n📍 Local IP: {local_net['local_ip']}")
    else:
        print("\n⚠️  Tidak dapat mendeteksi IP lokal")
    
    print(f"🔍 Target Network: {network_range}\n")
    
    # Jalankan network scan
    hosts = scan_network(network_range)
    
    if not hosts:
        print("⚠️  Tidak ada host aktif yang ditemukan\n")
        print("="*80 + "\n")
        return
    
    print(f"\n📊 Total host aktif ditemukan: {len(hosts)}\n")
    print(f"{'No.':<4} {'IP Address':<16} {'Hostname':<30} {'Status':<10}")
    print("-"*80)
    
    for i, host in enumerate(hosts, 1):
        ip = host['ip']
        hostname = host['hostname'][:29]  # Truncate jika terlalu panjang
        status = host['status']
        
        print(f"{i:<4} {ip:<16} {hostname:<30} {status:<10}")
    
    print("="*80 + "\n")


def display_port_scan(ip_address):
    """
    Menampilkan hasil port scan dalam format yang rapi
    
    Args:
        ip_address (str): IP address untuk di-scan
    """
    print("\n" + "="*80)
    print("🔌 PORT SCANNER")
    print("="*80)
    
    # Cek nmap
    if not check_nmap_installed():
        print("\n❌ NMAP TIDAK TERINSTALL")
        print("\nUntuk menggunakan fitur port scanning, silakan install nmap:")
        print("   Ubuntu/Debian: sudo apt install nmap")
        print("   CentOS/RHEL:   sudo yum install nmap")
        print("   macOS:         brew install nmap")
        print("="*80 + "\n")
        return
    
    print(f"\n🎯 Target: {ip_address}\n")
    
    # Jalankan port scan
    open_ports = scan_ports(ip_address, top_ports=20)
    
    if not open_ports:
        print("ℹ️  Tidak ada port yang terbuka pada top 20 port populer\n")
        print("="*80 + "\n")
        return
    
    print(f"\n📊 Total port terbuka: {len(open_ports)}\n")
    print(f"{'No.':<4} {'Port':<8} {'Protocol':<10} {'State':<10}")
    print("-"*80)
    
    for i, port_info in enumerate(open_ports, 1):
        port = port_info['port']
        protocol = port_info['protocol']
        state = port_info['state']
        
        print(f"{i:<4} {port:<8} {protocol:<10} {state:<10}")
    
    print("="*80 + "\n")


def scan_quick():
    """
    Melakukan quick scan untuk network lokal (192.168.1.0/24)
    """
    display_scan_results("192.168.1.0/24")


def scan_advanced():
    """
    Mode advanced scan dengan input dari user
    """
    print("\n" + "="*80)
    print("🌐 ADVANCED NETWORK SCANNER")
    print("="*80)
    
    print("\n1. Network Scan (Discover hosts)")
    print("2. Port Scan (Scan specific host)")
    print("3. Kembali ke menu utama")
    
    choice = input("\nPilih opsi: ").strip()
    
    if choice == '1':
        network = input("Masukkan range network (contoh: 192.168.1.0/24): ").strip()
        if network:
            display_scan_results(network)
    
    elif choice == '2':
        ip = input("Masukkan IP address untuk di-scan: ").strip()
        if ip:
            display_port_scan(ip)
    
    elif choice == '3':
        return
    
    else:
        print("❌ Opsi tidak valid")


if __name__ == "__main__":
    scan_quick()
