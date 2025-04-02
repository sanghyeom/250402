# ex_50.py 인공신경망 완전레이어 구현
# 입력 숫자가 input_dim 출력숫자가 output_dim
# weight는 2차원 리스트 , bias는 1차원 리스트
# 리스트 초기화에는 ramdom.random()사용
# Forword () 함수에서 행렬곱과 행렬합 수행하는 코드로 출력값 계산

import random

class Linear :
    def __init__(self, in_feature, out_feature):
        self.bias = []
        self.weight_in=[] 
        for i in range(out_feature):
            self.weight=[] 
            self.bias.append(random.random())
            self.weight_in.append(random.random())
            for j in range(in_feature):
                self.weight.append(self.weight_in)
        print(self.bias)
        print(self.weight)
    
    def matumul(self, A, B):
        row = len(A)
        B= self.weight
        C= self.bias
        for i in range(row):
            for j in range(len(A[i])):
                for h in range(len(A[i])):
                    C[i][j] += A[i][h]*B[h][j]
        return C

    def forward(self, x):
        Z =self.matumul(x, self.weight)
        # x= self.weight + self.bais
        for i in range(len(Z)):
            for j in range(len(self.bias)):
                Z[i][j]= Z[i][j] + self.bias[j]


linear = Linear(3,2)
x = [[1,2,3],[4,5,6]]

print(linear.forward(x))

 
