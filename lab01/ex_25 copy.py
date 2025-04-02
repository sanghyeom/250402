line = "-"*40
ID = "python"
PW = "abcd"
check_ID = ''
check_PW = ''

# for i in range(1,6) :
    
print(line)
check_ID = input(f"회원 ID : ")
for i in range(1,6) :
    if i==5 :
        if ID == check_ID:
            check_PW = input(f"회원 PW : ")
            if PW == check_PW : 
                print("로그인 성공")
                break
            elif PW != check_PW :
                print("비밀번호가 틀렸습니다.")
                print(f"남은기회 {5-i}/5\n로그인이 잠겼습니다.")
        else: 
            print("ID를 찾을 수 없습니다.")
    else :
        if ID == check_ID:
            check_PW = input(f"회원 PW : ")
            if PW == check_PW : 
                print("로그인 성공")
                break
            elif PW != check_PW :
                print("비밀번호가 틀렸습니다.")
                print(f"남은기회 {5-i}/5")
        else: 
            print("ID를 찾을 수 없습니다.")
print(line)

