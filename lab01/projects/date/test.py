# BLANK
import random

# 각 월의 일수를 저장하는 리스트
MONTH_DAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

# [!주의!] 이 함수의 코드를 수정하지 마세요
# 주어진 해가 평년인지 윤년인지 검사하는 함수
# 평년이면 365일, 윤년이면 366일
def is_leap_year(year):
    # 1700은 4의 배수, 100의 배수, 400의 배수 아니므로 평년
    # 1600은 4의 배수, 100의 배수, 400의 배수 이므로 윤년
    # 1996은 4의 배수, 100의 배수 아님, 400의 배수 아님 윤년
    if year %  4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False








#####################################################################      
# Mission 1 : 년도와 달을 입력받아 그 달의 날 수를 반환하는 함수를 완성하시오.
# 주어진 월의 총 일수를 반환하는 함수
# 단 이때 2월은 윤년이면 29, 평년이면 28을 반환해야 하므로 연도도 함께 전달 받음
# is_leap_year(year) 함수를 활용하시오.
# 함수가 완셩되었다면 이 파일을 메인 실행파일로 실행하여
# 1988년, 1995년에 대해서 제대로 된 결과를 출력하는지 확인하시오.
def get_month_days(year, month):
    # 달의 날짜 수에 +1해야되는 경우를 여기서 처리하시오.
    # if 문에서 year이 윤년인지는 이미 체크되고 있고 
    # month가 2월인지 추가로 체크하는 논리식을 and로 연결하시오.



    if is_leap_year(year) and month==2 :
        # 이 함수가 전달받은 month 변수를 이용하여 
        # 모든 달의 날짜가 적혀있는 MONTH_DAYS에서 해당 달의 날짜를 
        # 조회 하시오.
        return MONTH_DAYS[month] + 1
    else:
        return MONTH_DAYS[month]
    









days_part_3 = 0

    # 1월 부터 현재 달 이전 달까지 산 날수를 모두 계산해서
    # days_part_3에 저장
for m in range(1, 1+1):
    print(m)
    # days_part_3 += get_month_days(2025, m)
        
    # step 3: 현재 달의 산 날 수를 days_part_3에 더함
# days_part_3 += cur_day