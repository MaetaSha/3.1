import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

fs = 8000
[n, w] = sig.buttord(1200 / 4000, 1500 / 4000, 1, 50)
[b, a] = sig.butter(n, w, btype='highpass')
w, h = sig.freqz(b, a, 512, fs=fs)
z, p, k = sig.tf2zpk(b, a)

plt.subplot(3, 1, 1)
plt.plot(w, np.abs(h))

plt.subplot(3, 1, 2)
plt.plot(w, np.unwrap(np.angle(h)))

plt.subplot(3, 1, 3)
plt.scatter(np.real(z), np.imag(z), marker='o', edgecolors='b')
plt.scatter(np.real(p), np.imag(p), marker='x', color='b')
plt.tight_layout()
plt.show()