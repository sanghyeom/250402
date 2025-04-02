# ex_46.py 로또 번호 추출기
# random.randrange(1,46)을 사용하여 무작위수 6개를 봅아 로또 번호를 추출하는 함수 만들기
# 인자 n을 설정하여 n에 설정된 만큼의 게임 만들기 (기본값1)
# 반환값을 2차우너 리스트로 반환하기

# import random
# lottery = []
# for i in range(6):
#     n = random.randrange(1,46)
#     lottery.append(n) 
def lottoo() :
    import random
    lottery = []
    while len(lottery) < 6:
        n = random.randrange(1,46)
        lottery.append(n)
        if lottery.count(n)>1 : 
            lottery.remove(n)
    return lottery

N = int(input('몇게임을 돌리시겠습니까?'))
game = []
while len(game)<N:
    game.append(lottoo())
print(game)
