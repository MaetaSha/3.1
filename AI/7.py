import pandas as pd
import numpy as np
data=pd.read_csv('data.csv')
print(data)

# leave the last column
concept=np.array(data)[:,:-1]
# only access the last column
target=np.array(data)[:,-1]

def train(concept,target):
    for i,value in enumerate(target):
        if value.lower()=='yes':
            specific_h=concept[i].copy()
            break
    for i,value in enumerate(concept):
        if target[i].lower()=='yes':
            for x in range(len(specific_h)):
                if value[x]!=specific_h[x]:
                    specific_h[x]='?'
                else:
                    pass;
    return specific_h

result=train(concept,target)
print(result)

day=input("Enter 6 word to check:")
day=day.split()
check=True

for i in range(len(result)):
    if result[i]=='?'or result[i]==day[i]:
        check=True;
    else:
        check=False;
        break;
if check:
    print("Enjoy sport")
else:
    print("Not Possible")
