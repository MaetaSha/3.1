import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('risk.csv')
print(df)
print("\n")
x = df[['speed']]
y = df['risk']
print(x)
print("\n")
print(y)

plt.scatter(df['speed'],df['risk'])
plt.xlabel('Speed of Car')
plt.ylabel('Risk on driving')
plt.title('Car driving speed risk')


from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=.40,random_state=1)
print(xtrain)
print("\n")
print(xtest)
print("\n")
print(ytrain)
print("\n")
print(ytest)
print("\n")

#60% For training and 40% for test
#xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=.40,random_state=1)
#xtrain
#xtest

#ytrain
#ytest

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(xtrain,ytrain)

reg.predict(xtest)
print(ytest)

plt.scatter(df['speed'],df['risk'],marker='*',color='red')
plt.xlabel('Speed of Car')
plt.ylabel('Risk on driving')
plt.title('Car driving speed risk')
plt.plot(df.speed,reg.predict(df[['speed']]))
print(reg.predict([[180]]))
regcof = reg.coef_
print(regcof)
reginter = reg.intercept_
print(reginter)
m = regcof*100+reginter
print(m)
plt.show()
