import pyshark


class MetroEthernetFrame:
    def __init__(self, src_mac, dst_mac, eth_type, data):
        self.src_mac = src_mac
        self.dst_mac = dst_mac
        self.eth_type = eth_type
        self.data = data

    def show_frame(self):
        return {
            "Source MAC": self.src_mac,
            "Destination MAC": self.dst_mac,
            "Ethernet Type": self.eth_type,
            "Data": self.data
        }


def capture_ethernet_frames(interface='eth0', timeout=10):
    print(f"Capturando tramas Ethernet en interfaz {interface} durante {timeout} segundos...")
    capture = pyshark.LiveCapture(interface=interface, display_filter='eth')
    capture.sniff(timeout=timeout)
    frames = []
    for packet in capture:
        frames.append(MetroEthernetFrame(
            src_mac=packet.eth.src if hasattr(packet, 'eth') else '',
            dst_mac=packet.eth.dst if hasattr(packet, 'eth') else '',
            eth_type=packet.eth.type if hasattr(packet, 'eth') else '',
            data=str(packet)
        ))
    return frames