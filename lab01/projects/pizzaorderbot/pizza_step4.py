

def main():
    print("빅데이터 피자 가게에 오신걸환영합니다.")
    menus = {
        '피자': ['페퍼로니 피자', '스테이크 피자', '시푸드 피자'],
        '토핑': ['햄', '페퍼로니', '트러플', '올리브', '새우'], ######## 추가
        '사이드': ['치즈오븐스파게티', '리조또', '치킨윙'],
        '음료': ['콜라', '스프라이트', '오렌지쥬스']
        }
    prices = {
        '피자': [29000, 32000, 32000],
        '토핑': [500, 500, 800, 300, 800], ######## 추가
        '사이드': [9900, 8900, 8900],
        '음료': [1000, 1000, 1000]
         }
    order = {'피자': [], '토핑': [],'사이드': [], '음료': []}
    categories = ['피자', '토핑','사이드','음료']
    i = 0
    current_category = categories[i]
    
    while True:
        print(f"\n{current_category}를 선택하세요. 수량 추가를 위해 여러번 선택가능합니다.")
        for idx in range(len(menus[current_category])):
            print(f"{idx+1}. {menus[current_category][idx]} ({prices[current_category][idx]}원)")
        choice = input('번호를 입력하고 Enter를 누르세요.(다음단계: n, 이전단계: p, 주문완료: f)')
        # if choice <len(menus[current_category]):
        #     print("넘었네?")
        if choice.isdigit():
            if int(choice) <len(menus[current_category]):
                index = int(choice)-1
                order[current_category].append(menus[current_category][index])
                print(f"선택된 메뉴: {menus[current_category][index]}")
            else :
                print("잘못된선택입니다. 다시 시도해주십시오.")
        elif choice == 'n' :
            if i<3 :
                i += 1
            else :
                i=i
            current_category = categories[i]    
        elif choice == 'p' :
            if i>0 :
                i -= 1
            else :
                i=i
            current_category = categories[i]    
        elif choice == 'f' :
            break       
        else :
            print("잘못된입력입니다. 다시 시도해주십시오.")
    return order
            
       
order = main()
print("\n주문내역 :")
print(order)


