# 初始化一个列表来存储提取的时间值
time_values = []

# 打开文件并读取每一行
with open('files/ping/ns-td.afrinic.net.txt', 'r') as file:
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

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
import pandas as pd

# 创建滞后图
plt.figure(figsize=(6, 6))
plt.scatter(time_values[:-1], time_values[1:], alpha=0.5)
plt.title('Lag Plot (Lag-1) of latency')
plt.xlabel('X(t)')
plt.ylabel('X(t+1)')
plt.grid(True)
plt.show()

# 创建自相关图
plt.figure(figsize=(10, 6))
pd.plotting.autocorrelation_plot(time_values, ax=plt.gca())
plt.title('Correlogram (Autocorrelation Plot) of latency')
plt.xlabel('Lag')
plt.grid(True)
plt.show()