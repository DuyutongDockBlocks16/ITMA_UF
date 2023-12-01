import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 定义数据文件的目录
directory_path = 'files/2_3_sample_files/output_sampled_ipv6.txt'

# 列名定义
columns = ['src', 'dst', 'pro', 'ok', 'sport', 'dport', 'packets', 'bytes', 'flows', 'first', 'latest']

# 读取文件并转换为 DataFrame
df = pd.read_csv(directory_path, sep='\t', header=None, names=columns)

# 计算每个用户（源IP地址）的聚合数据量
user_data_volume = df.groupby('src')['bytes'].sum().sort_values(ascending=False)
#
# # 取前180名用户的数据量
# top_users = user_data_volume.head(180)
#
# # 将其他用户的数据量汇总到 'Other Users'
# other_users_volume = user_data_volume.iloc[180:].sum()
# other_users_series = pd.Series([other_users_volume], index=['Other Users'])
#
# # 合并 top_users 和 other_users_series
# top_users_with_others = pd.concat([top_users, other_users_series])
#
# # 计算每个图表的大小
# chunk_size = int(np.ceil(len(top_users_with_others) / 4))
# user_chunks = [top_users_with_others[i:i + chunk_size] for i in range(0, len(top_users_with_others), chunk_size)]
#
# # 为每个部分绘制条形图
# for i, chunk in enumerate(user_chunks, start=1):
#     plt.figure(figsize=(12, 6))
#     chunk.plot(kind='bar', color='skyblue')
#     plt.title(f'User Aggregated Data Volume - Part {i}')
#     plt.xlabel('User IP Address')
#     plt.ylabel('Aggregated Data Volume (bytes)')
#     plt.xticks(rotation=90)
#     plt.tight_layout()
#     plt.yscale('log')
#     plt.show()


plt.figure(figsize=(12, 6))
user_data_volume.plot(kind='line', color='skyblue')
plt.title(f'User Aggregated Data Volume')
plt.ylabel('Aggregated Data Volume (bytes)')
plt.yscale('log')
ax = plt.gca()
ax.xaxis.set_visible(False)
plt.show()