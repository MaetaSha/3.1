import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt
from lcapy.discretetime import n
x = 1 / 16 ** n
Z = x.ZT()
print(Z)
x = Z.IZT()
print(x)
# Define the transfer function
num = [1, 0, 0, 1]
den = [1, 0, 2, 0, 1]
[z, p, k] = sig.tf2zpk(num, den)
# Plot the poles and zeros
plt.scatter(np.real(z), np.imag(z), edgecolors='b', marker='o')
plt.scatter(np.real(p), np.imag(p), color='b', marker='x')
# Add a unit circle
circle = plt.Circle((0, 0), 1, fill=False, color='r', linestyle='dotted')
plt.gca().add_patch(circle)
# Set axis limits and labels
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])
plt.axvline(0, color='black',linewidth=0.5)
plt.axhline(0, color='black',linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('Real')
plt.ylabel('Imaginary')
# Show the plot
plt.show()