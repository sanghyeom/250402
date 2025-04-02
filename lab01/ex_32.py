# ex_32.py 순서대로 출력하기
# 다음 순서대로 저장된 프로야구팀을 순서대로 순위를 매겨 출력하기
# 단, for team in teams 형식을 사용
# - team = [ '타이거즈', '라이온즈', '트윈즈', '베어즈', '위즈',
#            '랜더스','자이언츠','이글스','다이노스','히어로즈']

teams = ['타이거즈', '라이온즈', '트윈즈', '베어즈', '위즈','랜더스','자이언츠','이글스','다이노스','히어로즈']

# for team in teams:
#     print(f"{teams.index(team)+1}위 {team}")

# i=1
# for team in teams:
#     print(i , team)
#     i +=1 

for i,team in enumerate(teams):
    print(i+1 , team)