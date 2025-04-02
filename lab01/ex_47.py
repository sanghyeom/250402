# ex_47.py 성적처리
# ex_35에서 제시된 성적데이터를 적은 scores.xlsx를 pandas패키지로 읽어
# 성적처리 자동화하는 코드 작성

import pandas as pd 

df = pd.read_excel("./data/scores.xlsx")

# print(type(df))
# print(df.T.to_dict())
# for D in df.T.to_dict().values() :
#     print(D)
df = df.T.to_dict()
data = [v for k, v in df.items()]
print(data)

# ㅠㅠ data 함수 가져오면됌 ㅠ