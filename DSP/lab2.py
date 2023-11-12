import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

numerator_a = [1, 0, 0, 1]
denominator_a = [1, 2, 1, 0]

numerator_b = [4, 8, 10]
denominator_b = [2, 8, 18, 20]

sys_a = signal.TransferFunction(numerator_a, denominator_a)
zeros_a, poles_a, _ = signal.tf2zpk(numerator_a, denominator_a)

sys_b = signal.TransferFunction(numerator_b, denominator_b)
zeros_b, poles_b, _ = signal.tf2zpk(numerator_b, denominator_b)

# Plotting poles and zeros
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(np.real(zeros_a), np.imag(zeros_a), marker='o', color='b', label='Zeros')
plt.scatter(np.real(poles_a), np.imag(poles_a), marker='x', color='r', label='Poles')
plt.title('System a: Zeros and Poles')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(np.real(zeros_b), np.imag(zeros_b), marker='o', color='b', label='Zeros')
plt.scatter(np.real(poles_b), np.imag(poles_b), marker='x', color='r', label='Poles')
plt.title('System b: Zeros and Poles')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

plt.tight_layout()
plt.show()
