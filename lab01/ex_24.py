line = "-"*40
check_ID = ''
check_PW = ''
blank = "\n" * 100


print(blank)
print(line)
ID = input(f"회원가입\n사용하실 ID를 입력해주세요 : ")
PW = input(f"사용하실 ID의 PW를 입력해주세요 : ")
print(line)


print(blank)
while PW != check_PW :
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

