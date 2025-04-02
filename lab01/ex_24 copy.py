# ex_24.py while을 활용한 로그인 로직
# 사용자에게 패스워드를 성공할때까지 입력받는 로직을 while로 구현

line = "-"*40
ID = "python"
PW = "abcd"
check_ID = ''
check_PW = ''

while PW != check_PW :
    # print("\n" * 100)
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

