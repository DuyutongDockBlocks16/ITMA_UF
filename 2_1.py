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
df_combined = pd.concat(df_list, ignore_index=True)

# 按 'dport' 聚合数据，获取计数并按降序排列
dport_counts = df_combined['dport'].value_counts().sort_values(ascending=False).head(20)

# 绘制条形图
plt.figure(figsize=(12, 8))
bars = plt.bar(dport_counts.index.astype(str), dport_counts.values, color='skyblue')

# 在条形上方添加文本注释
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')

plt.title('Top 20 Flow Distribution by Destination Port (dport) Across All Files')
plt.xlabel('Destination Port')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()
