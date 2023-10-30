import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data from CSV file using pandas
#df = pd.read_csv('G:/car driving risk analysis.csv')  # Replace 'your_data.csv' with your actual CSV file name
x = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
# Corresponding output data (target)
y = np.array([11, 13, 12, 15, 17, 18, 18, 19, 20, 22])
# Calculate the mean of x and y
mean_x = np.mean(x)
mean_y = np.mean(y)
#n = np.array(df)
#print(n)
siz = np.size(x)
#print(siz)



# Calculate slope b and y-intercept a using the formula
# b = Σ(xi*yi)-n*(mean_x)(mean-y)/Σ(xi*x1)-n*(mean_x)^2
# a = ȳ - b * x̄
up = np.sum(x*y) - siz*mean_x*mean_y
low = np.sum(x*x) - siz*mean_x*mean_x
slope = up / low
intercept = mean_y - slope * mean_x
#print(numerator)
#print(denominator)


# Predict y values using the linear regression equation: y = mx + b
predicted_y = slope * x + intercept

# Plot the original data points
plt.scatter(x, y, color='blue', label='Actual Data')

# Plot the regression line
plt.plot(x, predicted_y, color='red', label='Regression Line')

# Add labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple Linear Regression')
plt.legend()

# Show the plot
plt.show()
