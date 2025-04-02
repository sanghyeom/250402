#정규분포확률밀도함수의 함수값 계산 
x = 0.1
μ = 1
σ = 0.5
e = 2.718
root2pi = 2.506

print (σ*root2pi)
print (1/(σ*root2pi))
print (e**1.62)
y = (1/(σ*root2pi))*(e**((-(x-μ)**2)/(2*σ**2)))
print(y)
# y1 = 1/(σ*root2pi)
# y3 = ((x-μ)**2 )/(2*σ**2)
# y2 = e**y3
# print (y1*y2)
