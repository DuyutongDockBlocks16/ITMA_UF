import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Plot flow length distribution (Histogram)
plt.figure(figsize=(10, 6))
sns.histplot(df['total_frames'], kde=False)
plt.title('Flow Length Distribution (Total Frames)')
plt.xlabel('Flow Length (Frames)')
plt.ylabel('Frequency')
plt.yscale('log')
plt.show()

# Plot the ECDF
plt.figure(figsize=(10, 6))
sns.ecdfplot(df['total_frames'])
plt.title('Empirical Cumulative Distribution Function (ECDF) of Flow Length')
plt.xlabel('Flow Length (Frames)')
plt.ylabel('ECDF')
plt.grid(True)  # Adding a grid for better readability
plt.show()

# Display key summary statistics
print("Key Summary Statistics (Total Frames):")
print(df['total_frames'].describe())