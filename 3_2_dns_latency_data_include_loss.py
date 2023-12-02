# awk '/Query time|Return|CURL/' anycastdns2.nic.td.txt > anycastdns2.nic.td.reloaded.txt
# awk '/Query time|Return|CURL/' ns-td.afrinic.net.txt > ns-td.afrinic.net.reloaded.txt
# awk '/Query time|Return|CURL/' pch.nic.td.txt > pch.nic.td.reloaded.txt

import re
import numpy as np

query_time_lines = []
curl_lines = []
delay_s = []

with open('files/dns_query/pch.nic.td.reloaded.txt', 'r') as file:
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
            delay_s.append(2000.0)
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


for i in range(0,len(query_time_lines)):
    delay = query_time_s[i]/1000 + connect_time_s[i]
    delay_s.append(delay)
delay_s.sort()
print(delay_s)

import matplotlib.pyplot as plt

# Assuming time_values contains the latency measurements
fig, ax = plt.subplots(figsize=(10, 6))
boxplot_dict = ax.boxplot(delay_s, patch_artist=True)

# Annotate median
medians = [median.get_ydata()[0] for median in boxplot_dict['medians']]
for tick, median in zip(ax.get_xticks(), medians):
    ax.text(tick, median, f'Median: {median:.2f}', ha='center', va='center', fontdict={'fontsize': 8, 'color': 'white'})

# Annotate quartiles
boxes = [box.get_path().vertices for box in boxplot_dict['boxes']]
for box in boxes:
    box_bottom = box[0, 1]
    box_top = box[2, 1]
    ax.text(box[0, 0], box_bottom, f'Q1: {box_bottom:.2f}', ha='center', va='top', fontdict={'fontsize': 8})
    ax.text(box[2, 0], box_top, f'Q3: {box_top:.2f}', ha='center', va='bottom', fontdict={'fontsize': 8})


# Set title and labels
ax.set_title('Latency Measurements Box Plot')
ax.set_ylabel('Latency (ms)')
ax.set_xlabel('Measurements')

# Show the plot
plt.show()