import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

N = 50
fs = 8000
fc = np.array([1200, 1400, 2500, 2600])
b = sig.firwin(N + 1, fc, fs=fs, window='hamming', pass_zero='bandpass')
w, h_freq = sig.freqz(b, fs=fs)
z, p, k = sig.tf2zpk(b, 1)

plt.subplot(3, 1, 1)
plt.plot(w, np.abs(h_freq))  # magnitude
plt.xlabel('frequency(Hz)')
plt.ylabel('Magnitude')

plt.subplot(3, 1, 2)
plt.plot(w, np.unwrap(np.angle(h_freq)))  # phase
plt.xlabel('frequency(Hz)')
plt.ylabel('Phase(angel)')

plt.subplot(3, 1, 3)
plt.scatter(np.real(z), np.imag(z), marker='o', edgecolors='b')
plt.scatter(np.real(p), np.imag(p), marker='x', color='b')
plt.show()