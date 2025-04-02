
# ex_38.py 성적처리
# 다음 사전으로 지정된 학생 별 성적 데이터를 실행결과에 제시된 형태로 바꾸기
# {'철수': [250, 83.333], '준호': [251, 83.667], '영희': [270, 90.0]}}
data =[
    {'name':'철수', 'math':85, 'eng':90, 'sci':75},
    {'name':'준호', 'math':73, 'eng':85, 'sci':93},
    {'name':'영희', 'math':92, 'eng':88, 'sci':90}
    ]
New_data = {}
for i in range(len(data)):
    Score_SUM = 0
    Score_AVG = 0
    Count = 0
    for value in data[i].values() :
        if type(value) == int :
            Score_SUM += value
            Count += 1
            Score_AVG = round((Score_SUM/Count),3) 
        New_data[data[i]['name']]= [Score_SUM,Score_AVG]
print(New_data)

        