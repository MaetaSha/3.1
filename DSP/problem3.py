import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz

fp1 = 0.2
fp2 = 0.35
fs1 = 1.0
fs2 = 0.425
fs = 2.0
M = 2

lowcut = min(fp1, fp2)
highcut = max(fp1, fp2)

b, a = butter(M, [lowcut, highcut], btype='band', fs=fs)

w, h = freqz(b, a, worN=8000)
plt.plot(0.5 * fs * w / np.pi, np.abs(h), 'b')
plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)], '--k')
plt.title('Bandpass filter frequency response')
plt.xlabel('Frequency')
plt.ylabel('Gain')
plt.grid()
plt.show()
