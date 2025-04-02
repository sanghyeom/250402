import random
selfbias = []
selfweight_1=[]
for i in range(2):
    
    selfweight =[]
    selfbias.append(random.random())
    selfweight_1.append(random.random())
    for j in range(3) :
        selfweight.append(selfweight_1)

print(selfbias)
print(selfweight)