import matplotlib.pyplot as plt
import re
import numpy as np
import pandas as pd

differences = []

# 读取文件
with open('files/tcp_connect_latency/sgp1.iperf.comnet-student.eu.txt', 'r') as file:
    for line in file:
        # 跳过包含时间的行
        if re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', line.strip()):
            continue

        # 提取并计算差值
        numbers = line.split(', ')
        if len(numbers) >= 2:
            try:
                diff = float(numbers[1]) - float(numbers[0])
                differences.append(diff)
            except ValueError:
                # 忽略无法转换为浮点数的行
                continue

# 创建滞后图
plt.figure(figsize=(6, 6))
plt.scatter(differences[:-1], differences[1:], alpha=0.5)
plt.title('Lag Plot (Lag-1) of latency')
plt.xlabel('X(t)')
plt.ylabel('X(t+1)')
plt.grid(True)
plt.show()

# 创建自相关图
plt.figure(figsize=(10, 6))
pd.plotting.autocorrelation_plot(differences, ax=plt.gca())
plt.title('Correlogram (Autocorrelation Plot) of latency')
plt.xlabel('Lag')
plt.grid(True)
plt.show()
