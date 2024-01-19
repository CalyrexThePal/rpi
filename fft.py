import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# File name of your CSV file
file_name = 'test1.csv'  # Replace with your file name

# Read the file and extract the sampling information
with open(file_name, 'r') as file:
    lines = file.readlines()
    sample_info = lines[2].strip()
    numbers = re.findall(r'\d+', sample_info)
    samples, sps = map(int, numbers)

# print(samples, sps)

# Read the voltage values, skipping the first three lines and the last line
voltage_data = pd.read_csv(file_name, skiprows=3, skipfooter=1, header=None, engine='python')
voltage_values = voltage_data.iloc[:, 0].values

# Perform FFT with the correct sampling rate
fft_values = np.fft.fft(voltage_values)
fft_freq = np.fft.fftfreq(samples, 1/sps)

# Prepare the frequency domain data for plotting
fft_magnitude = np.abs(fft_values)
positive_frequencies = fft_freq > 0
fft_freq_positive = fft_freq[positive_frequencies]
fft_magnitude_positive = fft_magnitude[positive_frequencies]

# Plotting the FFT result
plt.figure(figsize=(12, 6))
plt.plot(fft_freq_positive, fft_magnitude_positive)
plt.title('Frequency Spectrum of the Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid()
plt.show()