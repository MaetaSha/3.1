import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# Specifications
fs = 10000  # Sampling rate
N = 67  # Order of filter
fc = 1500  # Passband edge frequency in Hz
transition_width = 500  # Transition width in Hz
# Design the filter using Blackman window
b = sig.firwin(N + 1, fc,transition_width, fs=fs, window='blackman', pass_zero='lowpass')

# Compute frequency response
w, h_freq = sig.freqz(b, fs=fs)

# Convert filter coefficients to zeros and poles
z, p, k = sig.tf2zpk(b, 1)

# Plot magnitude response
plt.figure(1)
plt.subplot(3, 1, 1)
plt.plot(w, np.abs(h_freq), color='r')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Response')

# Plot phase response
plt.figure(2)
plt.plot(w, np.unwrap(np.angle(h_freq)))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (angle)')
plt.title('Phase Response')

# Plot pole-zero plot
plt.figure(3)
plt.scatter(np.real(z), np.imag(z), marker='o', edgecolors='r', label='Zeros')
plt.scatter(np.real(p), np.imag(p), marker='x', color='b', label='Poles')
plt.title('Pole-Zeros Plot')
plt.xlabel('Real part')
plt.ylabel('Imaginary part')
plt.legend()

plt.show()