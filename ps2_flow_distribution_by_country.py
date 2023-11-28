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

df = pd.read_csv('files/final_a.txt', sep='\s+', skiprows=5, header=None, skipfooter=1, engine='python')

new_column_names = ["first_ip_interface", "arrow", "second_ip_interface", "ld_frames", "ld_bytes", "ld_bytes_unit",
                    "rd_frames", "rd_bytes", "rd_bytes_unit", "total_frames", "total_bytes", "total_bytes_unit",
                    "start", "duration"]

df.columns = new_column_names

pd.set_option('display.max_columns', None)

df = df.assign(**df.apply(convert_to_byte, axis=1))

geoip_reader = Reader('others/GeoLite2-Country.mmdb')

def get_country(ip):
    try:
        response = geoip_reader.country(ip)
        return response.country.name
    except:
        return "Unknown"

df['country'] = df['second_ip_interface'].str.split(':').str[0].apply(get_country)

country_traffic = df.groupby('country').size()

plt.figure(figsize=(12, 8))
country_traffic.plot(kind='bar')
plt.xlabel('Country')
plt.ylabel('Total Traffic (Bytes)')
plt.title('Flow Distribution by Country')
plt.xticks(rotation=45)

# 添加数字标签
for i, v in enumerate(country_traffic):
    plt.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

plt.show()
