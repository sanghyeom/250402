# ex_33.py 성적처리
# 다음 두 리스트는 지수와 만수의 국어, 수학, 영어 점수를 저장하고 있다.
# 성적 처리를 위해 각 과목의 총점을 저장한 리스트를 만들어보자
  
jisoo = ['90','85','93']
mansoo = ['78','92','89']

# print(f"#        국어, 수학, 영어")
# print(f"jisoo =  [{jisoo[0]},    {jisoo[1]},  {jisoo[2]}]")
# print(f"mansoo = [{mansoo[0]},    {mansoo[1]},  {mansoo[2]}]")

# all = jisoo
# for i in range(len(jisoo)):
#     all[i] = int(jisoo[i]) + int(mansoo[i])

# print(f" 국어,수학,영어")
# print(all)

##################################################
# scores = [[90, 85, 93],
#           [78, 92, 89]]
# SUB_total = [0]*len(scores[0])
# P_total = [0]*len(scores)
# for i in range(len(scores)):
#     for j in range(len(scores[0])):
#         P_total[i] += scores[i][j]
#         SUB_total[j] += scores[i][j]
# print(f"\n        국어 수학 영어")
# print("과목별",SUB_total)
# print(f"        지수, 만수")
# print("학생별",P_total)


scores = [[90, 85, 93],
          [78, 92, 89]]
total_by_student = []
#st = 0, 1
for st in range(len(scores)):
    # print(scores[st])
    total = 0
    for sb in range(len(scores[0])):
        # print(scores[st][sb])
        total += scores[st][sb]
    total_by_student.append(total)
print(total_by_student)

total_by_subjects = []
for sb in range(len(scores[0])):
    # print(scores[st])
    total = 0
    for st in range(len(scores)):
        # print(scores[st][sb])
        total += scores[st][sb]
    total_by_subjects.append(total)
print(total_by_subjects)