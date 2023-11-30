import pandas as pd
import matplotlib.pyplot as plt
import glob

# 定义数据文件的目录
directory_path = 'files/my_files/'

# 列名定义
columns = ['src', 'dst', 'pro', 'ok', 'sport', 'dport', 'packets', 'bytes', 'flows', 'first', 'latest']

# 使用 glob 来获取目录下的所有文件路径
file_paths = glob.glob(directory_path + '*.t2')

# 读取所有文件并合并为一个 DataFrame
df_list = [pd.read_csv(file, sep='\t', header=None, names=columns) for file in file_paths]
df_combined = pd.concat([df for df in df_list if not df.empty], ignore_index=True)

# 确保 'first' 列是 datetime 类型
df_combined['first'] = pd.to_datetime(df_combined['first'], unit='s')

# 按分钟和小时汇总流量
df_combined.set_index('first', inplace=True)
traffic_per_minute = df_combined.resample('T')['bytes'].sum()
traffic_per_hour = df_combined.resample('H')['bytes'].sum()

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