# # ex_str.py
# #자동완성에서 줄넘김은 control + enter

# s= "hello Python"
# print(s)

# s= 'hello Python'
# print(s)

# s= 'hello "EASY" Python'
# print(s)

# s= "hello \"EASY\" Python"
# print(s)
# # \" = 일반적인 문자다 라고 알려주는 너낌적 너낌 이스케이프 escape 한다라고표현

# s= "hello,\n \"EASY\" Python"
# print(s)
# #줄바꾸고 싶으면 \n

# print (type(s))

# s= """hello, 
#      "EASY" Python"""
# print(s)
# # """보이는 대로 출력 가넝~"""

# ############################
# # F- string
# ############################
# a = 10
# b = 20
# c = a * b
# # print('c: ',c,'SUCCESS')
# # print(f"C: {c} SUCCESS")

# print(f"{a} x {b} = {c:f}")


# d = 5.2
# e = 21.234
# f = d * e
# print(f"{d:5.2f} x {e:5.2f} = {f:.3f}")

# a= "hello"
# print(f"{a:_^10}")

s = "python"
print(type(s))

# count()
print(s.count('pythonpython'))

# find()
print (s.find('p'))# 처음만나는 p의 인덱스
print (s.find('x')) # 없으면 -1

# replace()
print(s.replace('python','PYTHON'))
print(s)

#split()
print(s.split()) # 기본값은 ' '
print(s.split(','))

L = ['python','java','C++']
print(','.join(L))

#strip()
s = " python "
print(f"|{s.strip()}|")
s = "@<python>!"
print(f"|{s.strip('<>!@')}|")

#isdigit, isalpha, isalnum
print(s.isdigit ())
print(s.isalpha())
print(s.isalnum())
#
s = 'PyThoOn'
print(s.upper())
print(s.lower())

