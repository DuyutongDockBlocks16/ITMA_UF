import pyshark
import matplotlib.pyplot as plt
from collections import Counter
from operator import itemgetter

tshark_path = 'D:\\0x00_Softwares\\Wireshark\\tshark.exe'
file_path = 'files/final_a.pcap'

cap = pyshark.FileCapture(file_path, tshark_path=tshark_path, keep_packets=True)

port_counts = Counter()
for packet in cap:
    if 'TCP' in packet or 'UDP' in packet:
        layer = packet.tcp if 'TCP' in packet else packet.udp
        port_counts[layer.dstport] += 1

cap.close()

sorted_port_counts = dict(sorted(port_counts.items(), key=itemgetter(1), reverse=True)[:20])

plt.figure(figsize=(10, 10))
plt.pie(sorted_port_counts.values(), labels=sorted_port_counts.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Top 20 Packet Distribution by Port Numbers')
plt.show()
