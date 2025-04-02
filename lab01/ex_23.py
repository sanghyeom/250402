# ex_23.py 아이디와 비밀번호를 모두 검사하는 로그인 로직
# 아이디를 입력받고 입력한 아이디가 맞으면 비번을 입력받음
# 입력받은 아이디가 틀리면 '그런 아이디는 존재하지않습니다.' 출력
# 아이디가 맞는 경우에만 비밀번호를 입력받고 로그인 성공 여부를 출력

line = "-"*40
check_ID = ''
check_PW = ''

print("\n" * 100)
print(line)
ID = input(f"회원가입\n사용하실 ID를 입력해주세요 : ")
PW = input(f"사용하실 ID의 PW를 입력해주세요 : ")
print(line)
print("\n" * 100)

print(line)
check_ID = input(f"회원 ID : ")
if ID == '' :
    print("확인가능한 ID 가 없습니다.")
else :
    if ID == check_ID:
        check_PW = input(f"회원 PW : ")
        if PW == check_PW : 
            print("로그인 성공")
        else:
            print("비밀번호가 틀렸습니다.")
    else: 
        print("ID를 찾을 수 없습니다.")
print(line)

