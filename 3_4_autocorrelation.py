import matplotlib.pyplot as plt
import re

# 从文件读取数据
with open('files/network_performance_measurement_tool/sgp1.iperf.comnet-student.eu.txt', 'r') as file:
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

import pandas as pd
# 创建滞后图
plt.figure(figsize=(6, 6))
plt.scatter(speeds_dl[:-1], speeds_dl[1:], alpha=0.5)
plt.title('Lag Plot (Lag-1) of DL Speed')
plt.xlabel('X(t)')
plt.ylabel('X(t+1)')
plt.grid(True)
plt.show()

# 创建自相关图
plt.figure(figsize=(10, 6))
pd.plotting.autocorrelation_plot(speeds_dl, ax=plt.gca())
plt.title('Correlogram (Autocorrelation Plot) of DL Speed')
plt.xlabel('Lag')
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 6))
plt.scatter(speeds_ul[:-1], speeds_ul[1:], alpha=0.5)
plt.title('Lag Plot (Lag-1) of UL Speed')
plt.xlabel('X(t)')
plt.ylabel('X(t+1)')
plt.grid(True)
plt.show()

# 创建自相关图
plt.figure(figsize=(10, 6))
pd.plotting.autocorrelation_plot(speeds_ul, ax=plt.gca())
plt.title('Correlogram (Autocorrelation Plot) of UL Speed')
plt.xlabel('Lag')
plt.grid(True)
plt.show()