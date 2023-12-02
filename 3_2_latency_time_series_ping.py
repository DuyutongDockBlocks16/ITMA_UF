import re
import matplotlib.pyplot as plt
from datetime import datetime

# ok1.iperf.comnet-student.eu
# sgp1.iperf.comnet-student.eu

# Initialize lists to store timestamps and time values
timestamps = []
time_values = []

# Open the file for reading
with open('files/ping/ok1.iperf.comnet-student.eu.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Use regular expressions to extract timestamp and time value
        match = re.search(r'\[(\d+\.\d+)\].*time=(\d+(\.\d+)?)', line)
        if match:
            timestamp = float(match.group(1))
            time = float(match.group(2))
            timestamps.append(timestamp)
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
