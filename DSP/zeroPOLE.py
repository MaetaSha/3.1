import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt

#question 1
num = [1,0,1]
den = [2,1,-0.5,0.25]
[z, p, k] = sig.tf2zpk(num, den)

# Plot the poles and zeros
plt.scatter(np.real(z), np.imag(z), edgecolors='b', marker='o')
plt.scatter(np.real(p), np.imag(p), color='b', marker='x')

# Add a unit circle
circle = plt.Circle((0, 0), 1, fill=False, color='b', linestyle='dotted')
plt.gca().add_patch(circle)

# Set axis limits and labels
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])
plt.axvline(0, color='black',linewidth=1)
plt.axhline(0, color='black',linewidth=1)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('Real')
plt.ylabel('Imaginary')

#question 2

num1 = [1,1,3/2,1/2]
den1 = [1,3/2,1/2]
[z1, p1, k1] = sig.tf2zpk(num1, den1)

# Plot the poles and zeros
plt.scatter(np.real(z1), np.imag(z1), edgecolors='r', marker='o')
plt.scatter(np.real(p1), np.imag(p1), color='r', marker='x')

# Add a unit circle
circle1 = plt.Circle((0, 0), 1.25, fill=False, color='r', linestyle='dotted')
plt.gca().add_patch(circle1)

# Set axis limits and labels
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])
plt.axvline(0, color='black',linewidth=1)
plt.axhline(0, color='black',linewidth=1)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('Real')
plt.ylabel('Imaginary')

# Show the plot
plt.show()