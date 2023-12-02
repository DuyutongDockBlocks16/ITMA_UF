import re
import numpy as np

query_time_lines = []
curl_lines = []

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



# Calculate First Packet Delay
first_packet_delay = delay_s[0]

# Calculate Mean Delay
mean_delay = np.mean(delay_s)

# Calculate the proportion of packets exceeding 2000 ms
proportion_outside = np.sum(np.array(delay_s) > 2000.0) / len(delay_s)

# Calculate the distance between quantiles
quantile_95 = np.quantile(delay_s, 0.95)
quantile_50 = np.quantile(delay_s, 0.5)
distance_between_quantiles = quantile_95 - quantile_50

# Print results
print(f"First Packet Delay: {first_packet_delay} ms")
print(f"Mean Delay: {mean_delay} ms")
print(f"Proportion of Packets Over 2000ms: {proportion_outside * 100:.2f}%")
print(f"Distance Between 0.95 and 0.50 Quantiles: {distance_between_quantiles} ms")