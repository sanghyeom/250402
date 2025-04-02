user_id = "python-master"
user_pw = "p1234"

AUTH = False

# 사용 승인 체크 데코레이터
def auth_required(func):
    def wrapper(*args, **kwargs):
        if AUTH == True:
            print("접근 승인")
            func(*args, **kwargs)
        else:
            print("접근 권한 없음")
    
    return wrapper

# 이 함수에 완성된 데코레이터를 적용해주세요.
@auth_required
def order_list():
    print("*********************")
    print("구매 리스트 출력")
    print("만두, 아이스크림, 콜라")
    print("*********************")

# 이 함수에 완성된 데코레이터를 적용해주세요.
@auth_required
def return_list():
    print("*********************")
    print("반품 리스트 출력")
    print("커피, 책")
    print("*********************")

# 이 함수에는 데코레이터를 적용하지 마세요.
def recommend_list():
    print("*********************")
    print("추천 목록 출력")
    print("참치, 라면, 피자")
    print("*********************")

def login():
    ######################### 함수밖,, 글로벌 ㅠㅠ
    global AUTH
    
    Check_id =input(" ID :")
    if Check_id == user_id :
        Check_pw =input(" PW :")
        if Check_pw == user_pw :
            AUTH = True
            print("로그인 성공")
        else : 
            print("PW 불일치")

    else:
        print("사용자id 확인할수 없음.")
            
while True:
    print("============================")
    print("[0] : 로그인")
    print("[1] : 구매 리스트")
    print("[2] : 교환 반품 리스트")
    print("[3] : 오늘의 추천 상품")
    c = input("메뉴 선택: ")

    if c == "1":
        order_list()
    elif c == "2":
        return_list()
    elif c == "3":
        recommend_list()
    elif c == "0":
        login()
    else:
        break