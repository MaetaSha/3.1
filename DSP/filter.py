import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz

fs = 1000  
t = np.arange(0, 1, 1/fs)  
signal = np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 10 * t) + np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 200 * t) + np.sin(2 * np.pi * 300 * t)

lowf = 40
highf = 60
order = 4

nyq = 0.5 * fs
low = lowf / nyq
high = highf / nyq
b, a = butter(order, [low, high], btype='band')
new_signal = lfilter(b, a, signal)

fft = np.fft.fft(new_signal)
freq = np.fft.fftfreq(len(fft), 1/fs)

plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, signal)
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t, new_signal)
plt.title('Filtered Signal (40-60 Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(freq, np.abs(fft))
plt.title('FFT of Filtered Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()

plt.tight_layout()
plt.show()
