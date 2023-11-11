import numpy as np
import matplotlib.pyplot as plt

f=10
fs=200
ts = 1/fs
t=np.arange(0, 1 , ts)
x=np.sin(2*np.pi*f*t)

plt.subplot(3,1,1)
plt.plot(t, x)
plt.xlabel('time (s)')
plt.ylabel('Amplitude')
plt.title('Original Signal')

plt.subplot(3,1,2)
plt.stem(t,x)
plt.xlabel('time (s)')
plt.ylabel('Amplitude')
plt.title('Samplrd  Signal')

xr= np.zeros_like(t)
for i in range (len(t)):
    xr += x[i]* np.sinc((t-i*ts)/ts)

plt.subplot(3,1,3)
plt.plot(t,xr)
plt.xlabel('time (s)')
plt.ylabel('Amplitude')
plt.title('Reconstructed  Signal')
plt.tight_layout()
plt.show()

