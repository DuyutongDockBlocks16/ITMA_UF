import matplotlib.pyplot as plt
import re

differences = []

# 读取文件
with open('files/tcp_connect_latency/sgp1.iperf.comnet-student.eu.txt', 'r') as file:
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

# Assuming time_values contains the latency measurements
fig, ax = plt.subplots(figsize=(10, 6))
boxplot_dict = ax.boxplot(differences, patch_artist=True)

# Annotate median
medians = [median.get_ydata()[0] for median in boxplot_dict['medians']]
for tick, median in zip(ax.get_xticks(), medians):
    ax.text(tick, median, f'Median: {median:.5f}', ha='center', va='center', fontdict={'fontsize': 8, 'color': 'white'})

# Annotate quartiles
boxes = [box.get_path().vertices for box in boxplot_dict['boxes']]
for box in boxes:
    box_bottom = box[0, 1]
    box_top = box[2, 1]
    ax.text(box[0, 0], box_bottom, f'Q1: {box_bottom:.5f}', ha='center', va='top', fontdict={'fontsize': 8})
    ax.text(box[2, 0], box_top, f'Q3: {box_top:.5f}', ha='center', va='bottom', fontdict={'fontsize': 8})


# Set title and labels
ax.set_title('Latency Measurements Box Plot')
ax.set_ylabel('Latency (ms)')
ax.set_xlabel('Measurements')

# Show the plot
plt.show()