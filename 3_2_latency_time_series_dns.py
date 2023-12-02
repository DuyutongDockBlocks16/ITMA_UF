# awk '/Query time|Return|CURL|^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}/' anycastdns2.nic.td.txt > anycastdns2.nic.td.reloaded.withtime.txt
# awk '/Query time|Return|CURL|^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}/' ns-td.afrinic.net.txt > ns-td.afrinic.net.reloaded.withtime.txt
# awk '/Query time|Return|CURL|^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}/' pch.nic.td.txt > pch.nic.td.reloaded.withtime.txt

import re
import numpy as np

query_time_lines = []
curl_lines = []
datetime = []

with open('files/dns_query/pch.nic.td.reloaded.withtime.txt', 'r') as file:
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
            datetime.pop(-1)
            continue
        if re.search("Query", striped_line):
            query_time_lines.append(striped_line)
        if re.search("CURL", striped_line):
            curl_lines.append(striped_line)
        if re.search("2023-", striped_line):
            datetime.append(striped_line)

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

print(delay_s)
print(datetime)

# Create a time series plot
plt.figure(figsize=(20, 8))  # Make the plot wider
plt.plot(datetime, delay_s, linestyle='-')
plt.xlabel('Date and Time')
plt.ylabel('Time (ms)')
plt.title('DNS latency Time Series')
plt.grid(True)

# Format x-axis to display both date and time, every 10th timestamp
# plt.xticks(range(0, len(datetime), 100), rotation=45, fontsize=8)
plt.xticks(rotation=90, fontsize=8)

# Show the plot
plt.show()
