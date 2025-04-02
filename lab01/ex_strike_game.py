self =[1,2,3]
digit = [1,4,3]


strike = 0
ball = 0


for i in range(0,3):
    if self[i] == digit[i]:
        strike += 1
    elif self[0] == digit[1]:
        ball=+1
    elif self[0] == digit[2]:
        ball=+1    
    elif self[1] == digit[2]:
        ball=+1
print(strike,ball)