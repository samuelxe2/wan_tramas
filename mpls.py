import pyshark

class MPLSLabel:
    def __init__(self, label, exp, s, ttl):
        self.label = label
        self.exp = exp        # QoS bits
        self.s = s            # Bottom of Stack bit
        self.ttl = ttl        # Time to Live

    def show_label(self):
        return {
            "Label": self.label,
            "EXP": self.exp,
            "S": self.s,
            "TTL": self.ttl
        }

def capture_mpls_labels(interface='eth0', timeout=10):
    print(f"Capturando etiquetas MPLS en interfaz {interface} durante {timeout} segundos...")
    capture = pyshark.LiveCapture(interface=interface, display_filter='mpls')
    capture.sniff(timeout=timeout)
    labels = []
    for packet in capture:
        if hasattr(packet, 'mpls'):
            labels.append(MPLSLabel(
                label=getattr(packet.mpls, 'label', ''),
                exp=getattr(packet.mpls, 'exp', ''),
                s=getattr(packet.mpls, 's', ''),
                ttl=getattr(packet.mpls, 'ttl', '')
            ))
    return labels