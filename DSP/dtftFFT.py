import numpy as np
import matplotlib.pyplot as plt

# MATLAB-style plot formatting
plt.style.use('ggplot')

# Define variables
n = np.arange(-1, 4)
x = np.arange(1, 6)
N = len(n)
k = np.arange(len(n))

# Calculate Fourier transform
X = np.sum(x * np.exp(-2j * np.pi * np.outer(n, k) / N), axis=1)
magX = np.abs(X)
angX = np.angle(X)
realX = np.real(X)
imagX = np.imag(X)

# Plot Fourier transform components
fig, axs = plt.subplots(2, 2, figsize=(8, 6))
axs[0, 0].plot(k, magX)
axs[0, 0].grid(True)
axs[0, 0].set_xlabel('Frequency in pi units')
axs[0, 0].set_title('Magnitude part')

axs[0, 1].plot(k, angX)
axs[0, 1].grid(True)
axs[0, 1].set_xlabel('Frequency in pi units')
axs[0, 1].set_title('Angle part')

axs[1, 0].plot(k, realX)
axs[1, 0].grid(True)
axs[1, 0].set_xlabel('Frequency in pi units')
axs[1, 0].set_title('Real part')

axs[1, 1].plot(k, imagX)
axs[1, 1].grid(True)
axs[1, 1].set_xlabel('Frequency in pi units')
axs[1, 1].set_title('Imaginary part')

plt.tight_layout()
plt.show()

# Perform FFT on signal
fs = 128
N = 256
T = 1 / fs
k = np.arange(N)
time = k * T
f = 0.25 + 2 * np.sin(2 * np.pi * 5 * k * T) + 1 * np.sin(2 * np.pi * 12.5 * k * T) + 1.5 * np.sin(
    2 * np.pi * 20 * k * T) + 0.5 * np.sin(2 * np.pi * 35 * k * T)

# Plot original signal
fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(time, f)
axs[0].set_title('Signal sampled at 128Hz')

# Calculate FFT and plot frequency components
F = np.fft.fft(f)
magF = np.abs(np.hstack((F[0] / N, F[1:N // 2] / (N / 2))))
hertz = k[0:N // 2] * (1 / (N * T))
axs[1].stem(hertz, magF)
axs[1].set_title('Frequency Components')
plt.tight_layout()
plt.show()