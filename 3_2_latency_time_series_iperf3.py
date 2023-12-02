import matplotlib.pyplot as plt
import re

differences = []
datetime = []

# sgp1.iperf.comnet-student.eu
# ok1.iperf.comnet-student.eu

# 读取文件
with open('files/tcp_connect_latency/ok1.iperf.comnet-student.eu.txt', 'r') as file:
    for line in file:
        if re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', line.strip()):
            datetime.append(line.strip())

        # 提取并计算差值
        numbers = line.split(', ')
        if len(numbers) >= 2:
            try:
                diff = float(numbers[1]) - float(numbers[0])
                differences.append(diff)

            except ValueError:
                # 忽略无法转换为浮点数的行
                continue

        # if len(datetime) != len(differences):
        #     print(datetime[-1])

# Create a time series plot
plt.figure(figsize=(30, 13))  # Make the plot wider
plt.plot(datetime, differences, linestyle='-')
plt.xlabel('Date and Time')
plt.ylabel('Time (ms)')
plt.title('IPERF3 latency Time Series')
plt.grid(True)

# Format x-axis to display both date and time, every 10th timestamp
plt.xticks(range(0, len(datetime), 20), rotation=45, fontsize=8)
# plt.xticks(rotation=90, fontsize=8)

# Show the plot
plt.show()