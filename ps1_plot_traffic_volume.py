import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = 'files/final_a.csv'

df = pd.read_csv(csv_file_path)

df['Time'] = pd.to_datetime(df['Time'], unit='s')

traffic_volume = df.groupby('Time')['Length'].sum().reset_index()

traffic_per_second = traffic_volume.set_index('Time').resample('S').sum().fillna(0)
traffic_per_minute = traffic_volume.set_index('Time').resample('T').sum().fillna(0)

plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
plt.plot(traffic_per_second.index, traffic_per_second['Length'], linestyle='-')
plt.title('Traffic Volume per Second')
plt.xlabel('Time (second)')
plt.ylabel('Traffic Volume (bytes)')
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
plt.plot(traffic_per_minute.index, traffic_per_minute['Length'], marker='o', linestyle='-', color='orange')
plt.title('Traffic Volume per Minute')
plt.xlabel('Time (minute)')
plt.ylabel('Traffic Volume (bytes)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
