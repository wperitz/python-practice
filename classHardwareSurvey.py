
import pandas as pd
import matplotlib.pyplot as plt

##### import data #####
data = pd.read_csv('MSDS-Orientation-Computer-Survey.csv')

##### Cleaning #####
data_cl = data.dropna()

##### Histograms #####
# 'CPU Cycle Rate (in GHz)'
plt.hist(data_cl['CPU Cycle Rate (in GHz)'])
plt.title('Histogram of CPU Cycle Rate')
plt.xlabel('CPU Cycle Rate (GHz)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# CPU Number of Cores
plt.hist(data_cl['CPU Number of Cores (int)'])
plt.title('Histogram of CPU Number of Cores')
plt.xlabel('CPU Number of Cores')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# RAM (in GB)
plt.hist(data_cl['RAM (in GB)'])
plt.title('Histogram of RAM (in GB)')
plt.xlabel('RAM (in GB)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Hard Drive Size (in GB)
plt.hist(data_cl['Hard Drive Size (in GB)'])
plt.title('Histogram of Hard Drive Size (in GB)')
plt.xlabel('Hard Drive Size (in GB)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# GPU CUDA Number of Cores (int)
plt.hist(data_cl['GPU CUDA Number of Cores (int)'])
plt.title('Histogram of GPU CUDA Number of Cores (int)')
plt.xlabel('GPU CUDA Number of Cores (int)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
