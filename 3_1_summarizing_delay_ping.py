# 初始化一个列表来存储提取的时间值
time_values = []

# 打开文件并读取每一行
with open('files/ping/sgp1.iperf.comnet-student.eu.txt', 'r') as file:
    for line in file:
        if 'time=' in line:
            # 找到包含 'time=' 的行，并分割字符串
            parts = line.split()
            for part in parts:
                if part.startswith('time='):
                    # 提取时间值，并移除 'ms'
                    time = part.split('=')[1].rstrip(' ms')
                    try:
                        # 将提取的时间值转换为浮点数并存储
                        time_values.append(float(time))
                    except ValueError:
                        # 如果转换失败，则跳过该值
                        continue

import numpy as np


# Calculate First Packet Delay
first_packet_delay = time_values[0]

# Calculate Mean Delay
mean_delay = np.mean(time_values)

# Calculate the proportion of packets exceeding 2000 ms
proportion_outside = np.sum(np.array(time_values) > 2000.0) / len(time_values)

# Calculate the distance between quantiles
quantile_95 = np.quantile(time_values, 0.95)
quantile_50 = np.quantile(time_values, 0.5)
distance_between_quantiles = quantile_95 - quantile_50

# Print results
print(f"First Packet Delay: {first_packet_delay} ms")
print(f"Mean Delay: {mean_delay} ms")
print(f"Proportion of Packets Over 2000ms: {proportion_outside * 100:.2f}%")
print(f"Distance Between 0.95 and 0.50 Quantiles: {distance_between_quantiles} ms")