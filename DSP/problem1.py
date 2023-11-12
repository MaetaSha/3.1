import numpy as np
import matplotlib.pyplot as plt
fs = 128
N = 256
T = 1 / fs
k = np.arange(N)
time = k * T

f = 0.25 + 2 * np.sin(2 * np.pi * 5 * k * T) + 1 * np.sin(2 * np.pi * 12.5 * k * T) + 1.5 * np.sin(2 * np.pi * 20 * k * T) + 0.5 * np.sin(2 * np.pi * 35 * k * T)

fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(time, f)
axs[0].set_title('Signal sampled at 128Hz')

F=np.fft.fft(f)
magF = np.abs(np.hstack((F[0] / N, F[1:N // 2] / (N / 2))))
hertz = k[0:N // 2] * (1 / (N * T))
axs[1].stem(hertz,magF)
axs[1].set_title('Frequency component')

plt.tight_layout()
plt.show()