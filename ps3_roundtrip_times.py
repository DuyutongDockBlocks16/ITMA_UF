import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 加载数据
file_path = 'files/final_a_tcptrace.csv'
df = pd.read_csv(file_path)

# 查找相关的列
rtt_avg_columns = ['RTT_avg_a2b', 'RTT_avg_b2a']
retrans_max_columns = ['max_#_retrans_a2b', 'max_#_retrans_b2a']

# 分析 RTT 平均值与最大重传次数的关系
for rtt_col, retrans_col in zip(rtt_avg_columns, retrans_max_columns):
    # 绘制散点图来查看这两个变量之间的关系
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df[rtt_col], y=df[retrans_col])
    plt.title(f'Relationship between {rtt_col} and {retrans_col}')
    plt.xlabel('Average RTT')
    plt.ylabel('Max Number of Retransmissions')
    plt.show()

    # 计算相关系数
    correlation = df[rtt_col].corr(df[retrans_col])
    print(f"Correlation between {rtt_col} and {retrans_col}: {correlation}")
