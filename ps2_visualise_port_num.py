import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

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

df = pd.read_csv('files/final_a.txt', sep='\s+', skiprows=5, header=None, skipfooter=1, engine='python')

new_column_names = ["first_ip_interface", "arrow", "second_ip_interface", "ld_frames", "ld_bytes", "ld_bytes_unit",
                    "rd_frames", "rd_bytes", "rd_bytes_unit", "total_frames", "total_bytes", "total_bytes_unit",
                    "start", "duration"]

df.columns = new_column_names

pd.set_option('display.max_columns', None)

df = df.assign(**df.apply(convert_to_byte, axis=1))

df['port'] = df['second_ip_interface'].str.split(':').str[1].astype(str)

port_flow_count = df.groupby('port').size().reset_index(name='count')
port_flow_count = port_flow_count.sort_values(by='count', ascending=False)

plt.figure(figsize=(10, 6))
bar_plot = plt.bar(port_flow_count['port'], port_flow_count['count'])

for bar in bar_plot:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), va='bottom', ha='center')

plt.xlabel('Port Number')
plt.ylabel('Number of Flows')
plt.title('Flow Count Distribution by Port Numbers (Descending)')
plt.xticks(rotation=45)
plt.show()