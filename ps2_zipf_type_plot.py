import pandas as pd
import matplotlib.pyplot as plt
from geoip2.database import Reader

def convert_to_byte(row):
    units = {'bytes': 1, 'kb': 1024, 'mb': 1024**2}

    try:
        ld_bytes_unit = str(row['ld_bytes_unit']).lower()
        factor = units[ld_bytes_unit]
        ld_kb = row['ld_bytes'] * factor

        rd_bytes_unit = str(row['rd_bytes_unit']).lower()
        factor = units[rd_bytes_unit]
        rd_kb = row['rd_bytes'] * factor

        total_bytes_unit = str(row['total_bytes_unit']).lower()
        factor = units[total_bytes_unit]
        total_kb = row['total_bytes'] * factor

        return pd.Series({'ld_bytes': ld_kb, 'rd_bytes': rd_kb, 'total_bytes': total_kb, 'server_ip': row['second_ip_interface']})
    except KeyError as e:
        print(f"Error processing row {row}: {e}")
        raise ValueError("Invalid unit. Supported units are 'bytes', 'kb', 'mb.")

df = pd.read_csv('files/part2.txt', sep='\s+', skiprows=5, header=None, skipfooter=1, engine='python')

new_column_names = ["first_ip_interface", "arrow", "second_ip_interface", "ld_frames", "ld_bytes", "ld_bytes_unit",
                    "rd_frames", "rd_bytes", "rd_bytes_unit", "total_frames", "total_bytes", "total_bytes_unit",
                    "start", "duration"]

df.columns = new_column_names

pd.set_option('display.max_columns', None)

df = df.assign(**df.apply(convert_to_byte, axis=1))

# 生成源-目的地对
df['src_dst_pair'] = df['first_ip_interface'] + ' - ' + df['second_ip_interface']

# 计算每个对的总数据量和流量次数
traffic_data = df.groupby('src_dst_pair')['total_bytes'].sum()
flow_counts = df.groupby('src_dst_pair').size()

# 对数据进行排序
sorted_traffic_data = traffic_data.sort_values(ascending=False)
sorted_flow_counts = flow_counts.sort_values(ascending=False)

# 绘制数据量的 Zipf 图
plt.figure(figsize=(10, 6))
plt.plot(sorted_traffic_data.values)
plt.xlabel('Source-Destination Pairs')
plt.ylabel('Total Data Volume (Bytes)')
plt.title('Zipf Plot of Data Volume by Source-Destination Pairs')
# plt.yscale('log')
# plt.xscale('log')
plt.show()

# 绘制流量的 Zipf 图
plt.figure(figsize=(10, 6))
plt.plot(sorted_flow_counts.values)
plt.xlabel('Source-Destination Pairs')
plt.ylabel('Number of Flows')
plt.title('Zipf Plot of Flows by Source-Destination Pairs')
# plt.yscale('log')
# plt.xscale('log')
plt.show()