d = { '1':'value1' ,'2':'value2'}

print(d)

# 기존값 업데이트
d['foo'] = 'foo@kdt.co.kr'
# 리스트 추가 가능
d['list'] = [1,2,3,4,5]

print(d)
d['list'] = ''

print(d)