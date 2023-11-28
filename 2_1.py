import pandas as pd
import matplotlib.pyplot as plt

# Path to the flow data file
file_path = 'files/my_15-3-0500.t2'

# Column names for the data
columns = ['src', 'dst', 'pro', 'ok', 'sport', 'dport', 'packets', 'bytes', 'flows', 'first', 'latest']

# Read the data from the text file
df = pd.read_csv(file_path, sep='\t', header=None, names=columns)

# Aggregate the data by 'dport' to get the counts and sort them in descending order
dport_counts = df['dport'].value_counts().sort_values(ascending=False).head(20)

# Plot for 'dport'
plt.figure(figsize=(12, 8))
bars = plt.bar(dport_counts.index.astype(str), dport_counts.values, color='skyblue')

# Add the text annotations on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')

plt.title('Top 20 Flow Distribution by Destination Port (dport)')
plt.xlabel('Destination Port')
plt.ylabel('Frequency')
plt.xticks(rotation=45)  # Rotate the x labels for better readability
plt.show()