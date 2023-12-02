import matplotlib.pyplot as plt
import re

differences = []

# 读取文件
with open('files/tcp_connect_latency/ok1.iperf.comnet-student.eu.txt', 'r') as file:
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

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# 计算概率密度函数
density = gaussian_kde(differences)
xs = np.linspace(min(differences), max(differences), 200)
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
sorted_data = np.sort(differences)
yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)

# 绘制CDF
plt.figure(figsize=(10, 6))
plt.plot(sorted_data, yvals, label='CDF')
plt.title('Cumulative Distribution Function of Latency')
plt.xlabel('Latency (ms)')
plt.ylabel('Cumulative Probability')
plt.legend()
plt.show()
