import pyshark

class SDHFrame:
    def __init__(self, header, pointer, payload, crc):
        self.header = header
        self.pointer = pointer
        self.payload = payload
        self.crc = crc

    def show_frame(self):
        return {
            "Header": self.header,
            "Pointer": self.pointer,
            "Payload": self.payload,
            "CRC": self.crc
        }

def capture_sdh_frames(interface='eth0', timeout=10):
    print(f"Capturando tramas SDH/SONET en interfaz {interface} durante {timeout} segundos...")
    capture = pyshark.LiveCapture(interface=interface, display_filter='sdh')
    capture.sniff(timeout=timeout)
    frames = []
    for packet in capture:
        frames.append(SDHFrame(
            header="HeaderSDH",
            pointer="PointerSDH",
            payload=str(packet),
            crc="CRC16"
        ))
    return frames