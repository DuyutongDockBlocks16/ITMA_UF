# 初始化一个列表来存储提取的时间值
time_values = []

# 打开文件并读取每一行
with open('files/ping/sgp1.iperf.comnet-student.eu.txt', 'r') as file:  # 请替换 'your_file.txt' 为您的文件名
    for line in file:
        if 'time=' in line:
            # 找到包含 'time=' 的行，并分割字符串
            parts = line.split()
            for part in parts:
                if part.startswith('time='):
                    # 提取时间值，并移除 'ms'
                    time = part.split('=')[1].rstrip(' ms')
                    try:
                        if float(time) > 2000.0:
                            time_values.append(float(2000.0))
                        else:
                            # 将提取的时间值转换为浮点数并存储
                            time_values.append(float(time))
                    except ValueError:
                        # 如果转换失败，则跳过该值
                        continue
        if 'packet loss' in line:
            # 找到包含 'packet loss' 的行，并分割字符串来提取百分数
            parts = line.split(',')
            for part in parts:
                if 'packet loss' in part:
                    # 提取百分比前的数字
                    percent_loss = part.split('%')[0].strip()
                    try:
                        # 将提取的百分比转换为浮点数并累加到总和
                        for i in range(0,int(float(percent_loss)/20.0)):
                            time_values.append(float(2000.0))
                            # print(f"{i} outlier detected")
                    except ValueError:
                        # 如果转换失败，则忽略该值
                        continue


import matplotlib.pyplot as plt

# Assuming time_values contains the latency measurements
fig, ax = plt.subplots(figsize=(10, 6))
boxplot_dict = ax.boxplot(time_values, patch_artist=True)

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
