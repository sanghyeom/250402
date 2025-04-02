# pizza_step1.py

def main():
    print("빅데이터 피자 가게에 오신걸환영합니다.")
    menus = ['페퍼로니 피자', '스테이크 피자', '시푸드 피자']
    price = [29000, 32000, 32000]
    order = []  
    # while I.isdigit() != True:
    while True:
        print("\n피자를 선택하세요. 수량 추가를 위해 여러번 선택가능합니다.")
        for idx, item in enumerate(menus):
            print(f"{idx+1}. {item} ({price[idx]}원)")
        choice = input('번호를 입력하고 Enter를 누르세요.(주문완료는 f를 누르세요.)')
        if choice.isdigit():
            index = int(choice)-1
            print(f"선택된 메뉴: {menus[index]}")
        elif choice == 'f' :
            break
        else :
            print("잘못된입력입니다. 다시 시도해주십시오.")

print("\n주문내역 :")
print(order)
main()