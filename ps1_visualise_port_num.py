import pyshark
import matplotlib.pyplot as plt
from collections import Counter

tshark_path = 'D:\\0x00_Softwares\\Wireshark\\tshark.exe'
file_path = 'files/part1.pcap'

cap = pyshark.FileCapture(file_path, tshark_path=tshark_path, keep_packets=True)

port_counts = Counter()
for packet in cap:
    if 'TCP' in packet or 'UDP' in packet:
        layer = packet.tcp if 'TCP' in packet else packet.udp
        port_counts[layer.dstport] += 1

cap.close()

plt.figure(figsize=(10, 10))
plt.pie(port_counts.values(), labels=port_counts.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Packet Distribution by Port Numbers')
plt.show()