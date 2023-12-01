import pandas as pd
import matplotlib.pyplot as plt
import glob
import numpy as np

# 定义数据文件的目录
directory_path = 'files/my_files/'

# 列名定义
columns = ['src', 'dst', 'pro', 'ok', 'sport', 'dport', 'packets', 'bytes', 'flows', 'first', 'latest']

# 使用 glob 来获取目录下的所有文件路径
file_paths = glob.glob(directory_path + '*.t2')

# 读取所有文件并合并为一个 DataFrame
df_list = [pd.read_csv(file, sep='\t', header=None, names=columns) for file in file_paths]
df_combined = pd.concat(df_list, ignore_index=True)

# 计算每个用户（源IP地址）的聚合数据量
user_data_volume = df_combined.groupby('src')['bytes'].sum().sort_values(ascending=False)

# # 将用户分成三个等分
# chunk_size = int(np.ceil(len(user_data_volume) / 3))
# user_chunks = [user_data_volume[i:i + chunk_size] for i in range(0, len(user_data_volume), chunk_size)]
#
# # 为每个部分绘制条形图
# for i, chunk in enumerate(user_chunks, start=1):
#     plt.figure(figsize=(12, 6))
#     chunk.plot(kind='bar', color='skyblue')
#     plt.title(f'User Aggregated Data Volume - Part {i}')
#     plt.xlabel('User IP Address')
#     plt.ylabel('Aggregated Data Volume (bytes)')
#     plt.xticks(rotation=90)  # Rotate the x labels for better readability
#     plt.tight_layout()  # Adjust layout to fit IP addresses
#     plt.yscale('log')
#     plt.show()


plt.figure(figsize=(12, 6))
user_data_volume.plot(kind='line', color='skyblue')
plt.title(f'User Aggregated Data Volume')
plt.ylabel('Aggregated Data Volume (bytes)')
plt.show()