import matplotlib.pyplot as plt
import re

# 从文件读取数据
with open('files/network_performance_measurement_tool/ok1.iperf.comnet-student.eu.txt', 'r') as file:
    data = file.read()

# 提取时间和速度数据
timestamps = []
speeds_dl = []
speeds_ul = []

# speed_receiver = dl
# speed_sender = ul

lines = data.split('\n')
last_is_date = 0
for line in lines:

    if re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line):
        if last_is_date == 0:
            timestamps.append(line.strip())
            last_is_date = 1
        elif last_is_date == 1:
            timestamps.pop(-1)
            timestamps.append(line.strip())

    striped_line = line.strip()
    if re.search("receiver", striped_line):
        items = striped_line.split()
        speeds_dl.append(float(items[6]))
        last_is_date = 0

    elif re.search("sender", striped_line):
        items = striped_line.split()
        speeds_ul.append(float(items[6]))
        last_is_date = 0

# 创建时间序列图
plt.figure(figsize=(12, 6))
plt.plot(timestamps, speeds_ul, label='UL Speed', marker='o')
plt.plot(timestamps, speeds_dl, label='DL Speed', marker='x')
plt.title('Time Series of Sender and Receiver Speed')
plt.xlabel('Timestamp')
plt.ylabel('Speed (Mbits/sec)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=90)
plt.tight_layout()

# 显示图形
plt.show()
