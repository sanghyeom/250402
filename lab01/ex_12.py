name = input('너의이름:')
score1 = int(input('국어점수:'))
score2 = int(input('영어점수:'))
score3 = int(input('수학점수:'))
score4 = int(input('과학점수:'))
total = score1+score2+score3+score4
ave = (total)/4
print(f"{name}의 총점은 {total} 평균은{ave}입니다.")
