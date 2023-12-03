import re
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

# ok1.iperf.comnet-student.eu
# sgp1.iperf.comnet-student.eu

# Initialize lists to store timestamps and time values
timestamps = []
time_values = []
ttls = []

# Open the file for reading
with open('files/ping/san2-us.ark.caida.org.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Use regular expressions to extract timestamp and time value
        match = re.search(r'\[(\d+\.\d+)\].*ttl=(\d+).*time=(\d+(\.\d+)?)', line)
        if match:
            timestamp = float(match.group(1))
            ttl = int(match.group(2))
            time = float(match.group(3))
            timestamps.append(timestamp)
            ttls.append(ttl)
            time_values.append(time)

# Convert timestamps to datetime objects with both date and time
datetime_timestamps = [datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') for ts in timestamps]

# Create a time series plot
plt.figure(figsize=(50, 18))  # Make the plot wider
plt.plot(datetime_timestamps, time_values, linestyle='-')
plt.xlabel('Date and Time')
plt.ylabel('Time (ms)')
plt.title('iperf3 latency Time Series')
plt.grid(True)

# Format x-axis to display both date and time, every 10th timestamp
plt.xticks(range(0, len(datetime_timestamps), 50), rotation=45, fontsize=15)

# Show the plot
plt.show()

# # 绘制散点图
# plt.scatter(ttls, time_values)
# plt.xlabel('TTL Values')
# plt.ylabel('Time Values')
# plt.title('Scatter Plot of TTL vs Time')
# plt.show()

# # 计算皮尔逊相关系数
# correlation_matrix = np.corrcoef(ttls, time_values)
# correlation_coefficient = correlation_matrix[0, 1]
# print("Pearson Correlation Coefficient:", correlation_coefficient)
#
# Create a time series plot
plt.figure(figsize=(12, 8))  # Make the plot wider
plt.plot(datetime_timestamps, ttls, linestyle='-')
plt.xlabel('Date and Time')
plt.ylabel('TTLs')
plt.title('TTL Time Series')
plt.grid(True)

plt.show()