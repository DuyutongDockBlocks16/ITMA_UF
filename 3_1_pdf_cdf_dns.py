# awk '/Query time|Return|CURL/' anycastdns2.nic.td.txt > anycastdns2.nic.td.reloaded.txt
# awk '/Query time|Return|CURL/' ns-td.afrinic.net.txt > ns-td.afrinic.net.reloaded.txt
# awk '/Query time|Return|CURL/' pch.nic.td.txt > pch.nic.td.reloaded.txt

import re
import numpy as np

query_time_lines = []
curl_lines = []

with open('files/dns_query/anycastdns2.nic.td.reloaded.txt', 'r') as file:
    skip_flag = 0
    for line in file:
        # 这里可以处理每一行的内容
        striped_line = line.strip()
        # print(striped_line)
        if skip_flag == 1:
            skip_flag = 0
            continue
        if re.search("Return", striped_line):
            skip_flag = 1
            continue
        if re.search("Query", striped_line):
            query_time_lines.append(striped_line)
        if re.search("CURL", striped_line):
            curl_lines.append(striped_line)

query_time_s = []
connect_time_s = []

for item in query_time_lines:
    item_split = item.split(" ")
    query_time = float(item_split[3])
    query_time_s.append(query_time)

for item in curl_lines:
    item_split = item.split(" ")
    connect_time = float(item_split[3])
    connect_time_s.append(connect_time)

delay_s = []
for i in range(0,len(query_time_lines)):
    delay = query_time_s[i]/1000 + connect_time_s[i]
    delay_s.append(delay)

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# 计算概率密度函数
density = gaussian_kde(delay_s)
xs = np.linspace(min(delay_s), max(delay_s), 200)
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
sorted_data = np.sort(delay_s)
yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)

# 绘制CDF
plt.figure(figsize=(10, 6))
plt.plot(sorted_data, yvals, label='CDF')
plt.title('Cumulative Distribution Function of Latency')
plt.xlabel('Latency (ms)')
plt.ylabel('Cumulative Probability')
plt.legend()
plt.show()
