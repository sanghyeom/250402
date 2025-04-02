line = "-"*40
ID = "python"
PW = "abcd"
check_ID = ''
check_PW = ''

print("\n" * 100)
print(line)
check_ID = input(f"회원 ID : ")

if ID == check_ID:
    check_PW = input(f"회원 PW : ")
    if PW == check_PW : 
        print("로그인 성공")
    else:
        print("비밀번호가 틀렸습니다.")
else: 
     print("ID를 찾을 수 없습니다.")
print(line)

