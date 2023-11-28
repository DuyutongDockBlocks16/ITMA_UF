import pandas as pd
import matplotlib.pyplot as plt

# Path to the flow data file
file_path = 'files/my_15-3-0500.t2'

# Column names for the data
columns = ['src', 'dst', 'pro', 'ok', 'sport', 'dport', 'packets', 'bytes', 'flows', 'first', 'latest']

# Read the data from the text file
df = pd.read_csv(file_path, sep='\t', header=None, names=columns)

# Compute the aggregate data volume for each user (src IP address)
user_data_volume = df.groupby('src')['bytes'].sum().sort_values(ascending=False)

# Plot a bar chart to visualise the distribution of user aggregated data
plt.figure(figsize=(12, 6))
user_data_volume.plot(kind='bar', color='skyblue')
plt.title('User Aggregated Data Volume')
plt.xlabel('User IP Address')
plt.ylabel('Aggregated Data Volume (bytes)')
plt.xticks(rotation=90)  # Rotate the x labels for better readability
plt.tight_layout()  # Adjust layout to fit IP addresses
plt.yscale('log')
plt.show()