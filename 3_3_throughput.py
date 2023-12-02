import re

speed_receiver = []
speed_sender = []

with open('files/network_performance_measurement_tool/sgp1.iperf.comnet-student.eu.txt', 'r') as file:
    for line in file:
        striped_line = line.strip()
        if re.search("receiver", striped_line):
            items = striped_line.split()
            speed_receiver.append(float(items[6]))
            print(striped_line)
        elif re.search("sender", striped_line):
            items = striped_line.split()
            speed_sender.append(float(items[6]))
            print(striped_line)

print(speed_receiver)
print(speed_sender)

# speed_receiver = dl
# speed_sender = ul

import matplotlib.pyplot as plt

# Assuming time_values contains the latency measurements
fig, ax = plt.subplots(figsize=(10, 6))
boxplot_dict = ax.boxplot(speed_receiver, patch_artist=True)

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
ax.set_title('Throughput Box Plot DL')
ax.set_ylabel('Throughput (Mbits/sec) DL')
ax.set_xlabel('Measurements')

# Show the plot
plt.show()


# Assuming time_values contains the latency measurements
fig, ax = plt.subplots(figsize=(10, 6))
boxplot_dict = ax.boxplot(speed_sender, patch_artist=True)

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
ax.set_title('Throughput Box Plot UL')
ax.set_ylabel('Throughput (Mbits/sec) UL')
ax.set_xlabel('Measurements')

# Show the plot
plt.show()

import numpy as np

# Calculate the mean, harmonic mean, geometric mean, and median for speed_receiver
mean_receiver = np.mean(speed_receiver)
harmonic_mean_receiver = 1 / np.mean(1 / np.array(speed_receiver))
geometric_mean_receiver = np.exp(np.mean(np.log(speed_receiver)))
median_receiver = np.median(speed_receiver)

# Calculate the mean, harmonic mean, geometric mean, and median for speed_sender
mean_sender = np.mean(speed_sender)
harmonic_mean_sender = 1 / np.mean(1 / np.array(speed_sender))
geometric_mean_sender = np.exp(np.mean(np.log(speed_sender)))
median_sender = np.median(speed_sender)

# Print the results
print("Mean of DL:", mean_receiver)
print("Harmonic mean of DL:", harmonic_mean_receiver)
print("Geometric mean of DL:", geometric_mean_receiver)
print("Median of DL:", median_receiver)

print("Mean of UL:", mean_sender)
print("Harmonic mean of UL:", harmonic_mean_sender)
print("Geometric mean of UL:", geometric_mean_sender)
print("Median of UL:", median_sender)