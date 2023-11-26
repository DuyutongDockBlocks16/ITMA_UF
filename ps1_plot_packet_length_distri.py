import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv_file_path = 'files/part1.csv'

df = pd.read_csv(csv_file_path)

plt.figure(figsize=(14, 7))

plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
bin_width = 100
bins = range(min(df['Length']), max(df['Length']) + bin_width, bin_width)
plt.hist(df['Length'], bins=bins, color='blue', alpha=0.7, log=True)
plt.title('Packet Length Distribution (Log Scale)')
plt.xlabel('Packet Length (bytes)')
plt.ylabel('Frequency (Log Scale)')

plt.subplot(1, 2, 2)
sorted_length = np.sort(df['Length'])
yvals = np.arange(1, len(sorted_length) + 1) / len(sorted_length)
plt.plot(sorted_length, yvals, marker='.', linestyle='none')
plt.title('Empirical Cumulative Distribution Function (ECDF)')
plt.xlabel('Packet Length (bytes)')
plt.ylabel('ECDF')

plt.tight_layout()
plt.show()

print("Summary statistics for packet lengths:")
print(df['Length'].describe())

# Summary statistics for packet lengths:
# count    178393.000000
# mean       1058.292758
# std        1753.207170
# min          42.000000
# 25%         218.000000
# 50%        1292.000000
# 75%        1292.000000
# max       65006.000000