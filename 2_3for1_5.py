import pandas as pd
import matplotlib.pyplot as plt
import glob

# 定义数据文件的目录
directory_path = 'files/2_3_sample_files/output_sampled_ipv6.txt'

# 列名定义
columns = ['src', 'dst', 'pro', 'ok', 'sport', 'dport', 'packets', 'bytes', 'flows', 'first', 'latest']

df = pd.read_csv(directory_path, sep='\t', header=None, names=columns)

# 确保 'first' 列是 datetime 类型
df['first'] = pd.to_datetime(df['first'], unit='s')

# 按分钟和小时汇总流量
df.set_index('first', inplace=True)
traffic_per_minute = df.resample('T')['bytes'].sum()
traffic_per_hour = df.resample('H')['bytes'].sum()


# 绘制流量随时间变化的图表 - 按分钟
plt.figure(figsize=(12, 6))
plt.plot(traffic_per_minute, label='Per Minute', color='blue')
plt.xlabel('Time')
plt.ylabel('Traffic Volume (bytes)')
plt.title('Traffic Volume Per Minute')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# 绘制流量随时间变化的图表 - 按小时
plt.figure(figsize=(12, 6))
plt.plot(traffic_per_hour, label='Per Hour', color='green')
plt.xlabel('Time')
plt.ylabel('Traffic Volume (bytes)')
plt.title('Traffic Volume Per Hour')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()