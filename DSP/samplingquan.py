import numpy as np
import matplotlib.pyplot as plt

# Function to perform quantization
def quantize_signal(signal, levels):
    quantized_signal = np.round(signal * (levels - 1)) / (levels - 1)
    return quantized_signal

# Function to perform coding (convert quantized signal to binary)
def code_signal(signal, bits):
    coded_signal = []
    for value in signal:
        # Convert each value to binary representation
        binary_code = format(int((value + 1) * (2**(bits-1))), f'0{bits}b')
        coded_signal.extend(map(int, binary_code))  # Append binary digits to the coded signal
    return np.array(coded_signal)

# Continuous-time signal
t_continuous = np.linspace(0, 1, 1000, endpoint=False)
x_continuous = np.sin(2 * np.pi * 5 * t_continuous) + 0.5 * np.sin(2 * np.pi * 20 * t_continuous)

# Sampling
fs = 20  # Sampling rate
t_discrete = np.arange(0, 1, 1/fs)
x_discrete = np.sin(2 * np.pi * 5 * t_discrete) + 0.5 * np.sin(2 * np.pi * 20 * t_discrete)

# Quantization
quantization_levels = 16  # Number of quantization levels (bits)
x_quantized = quantize_signal(x_discrete, quantization_levels)

# Coding
coding_bits = 8  # Number of bits for coding
x_coded = code_signal(x_quantized, coding_bits)

# Plotting
plt.figure(figsize=(14, 8))

plt.subplot(3, 1, 1)
plt.plot(t_continuous, x_continuous, label='Continuous Signal')
plt.stem(t_discrete, x_discrete, linefmt='r-', markerfmt='ro', basefmt='r-', label='Discrete Samples')
plt.title('Sampling Operation')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3, 1, 2)
plt.stem(t_discrete, x_quantized, linefmt='b-', markerfmt='bo', basefmt='r-', label=f'Quantized Signal ({quantization_levels} levels)')
plt.title('Quantization Operation')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3, 1, 3)
plt.stem(np.arange(len(x_coded)), x_coded, linefmt='g-', markerfmt='go', basefmt='r-', label=f'Coded Signal ({coding_bits} bits)')
plt.title('Coding Operation')
plt.xlabel('Time')
plt.ylabel('Binary Code')
plt.legend()

plt.tight_layout()
plt.show()