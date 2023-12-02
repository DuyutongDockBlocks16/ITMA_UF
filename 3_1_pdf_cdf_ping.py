# 初始化一个列表来存储提取的时间值
time_values = []

# 打开文件并读取每一行
with open('files/ping/ok1.iperf.comnet-student.eu.txt', 'r') as file:
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

# 计算概率密度函数
density = gaussian_kde(time_values)
xs = np.linspace(min(time_values), max(time_values), 200)
density.covariance_factor = lambda: .25
density._compute_covariance()

# 绘制PDF
plt.figure(figsize=(10, 6))
plt.plot(xs, density(xs), label='PDF')
plt.title('Probability Density Function of Latency')
plt.xlabel('Latency (ms)')
plt.ylabel('Density')
plt.legend()
plt.show()

# 计算CDF
sorted_data = np.sort(time_values)
yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)

# 绘制CDF
plt.figure(figsize=(10, 6))
plt.plot(sorted_data, yvals, label='CDF')
plt.title('Cumulative Distribution Function of Latency')
plt.xlabel('Latency (ms)')
plt.ylabel('Cumulative Probability')
plt.legend()
plt.show()
