import pyshark
import csv
from datetime import datetime

captured_data = []

def capture_mpls_packets(interface='eth0', timeout=10):
    print(f"Capturando paquetes MPLS en interfaz {interface} durante {timeout} segundos...")
    capture = pyshark.LiveCapture(interface=interface, display_filter='mpls')
    capture.sniff(timeout=timeout)

    for packet in capture:
        print("\n[MPLS Packet Capturado]")
        print(packet)
        captured_data.append({
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Packet": str(packet)
        })

def export_to_csv(filename='captured_packets.csv'):
    keys = captured_data[0].keys() if captured_data else []
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(captured_data)
    print(f"Datos exportados a {filename}")