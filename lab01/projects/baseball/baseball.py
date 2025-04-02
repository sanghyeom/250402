import random

class Digit3:
    def __init__(self):
        self.player_list = {}
        self.cur_player = None

    def init_game(self):
        ############################################################
        # 3자리 숫자 초기화
        # 각자리가 중복되면 안되고
        # 첫자리가 0이 되면 안되고
        # hint: 문자로 한 자리씩 숫자를 생성해서 0인지 검사하고 
        #       앞 숫자와 겹치는지 검사

        number_game_set = []
        while len(number_game_set) < 3:
            n = random.randrange(0,9)
            number_game_set.append(n)
        if number_game_set[0] == 0 :
            number_game_set.remove(0)
        if number_game_set.count(n)>1 : 
            number_game_set.remove(n)
        # return number_game_set

        ############################################################
        #                 
        
        # 위에서 초기화된 맞혀야 하는 숫자
        self.d = number_game_set
        
        # 개발 과정에서 내부적으로 초기화한 숫자를 화면에 뿌림
        print('init_game:', self.d)


    def q(self, digit):
        # digit: 사용자로부터 입력된 세자리수
        # digit이 self.d와 일치하는지 검사해서
        # 볼카운트를 다음과 같은 사전으로 만들어 반환
        # {'ball': 2, 'strike': 1}

        strike  = 0
        ball = 0

        ############################################################
        # self.d와 digit을 비교하여 볼카운트를 생성
        # hint: 숫자를 문자로 다루기..."123"
        #       str.count()함수 사용
        for i in range(0,3):
            if self.d[i] == digit[i]:
                strike += 1
            elif self.d[0] == digit[1]:
                ball=+1
            elif self.d[0] == digit[2]:
                ball=+1            
            elif self.d[1] == digit[2]:
                ball=+1
        ############################################################

        # 볼카운트가 저장된 변수를 리턴
        return {'ball': ball, 'strike': strike }
    
    def rank(self):
        # 현재 self.player_list에 저장된 플레이어들의 성적을 출력
        # 플레이어 "아이디 {점수}회 만에 성공" 형식으로 출력
        # self.payer_list 형식
        # {'플레이어1': 점수, '플레이어2': 점수}
        # hint: sorted()함수 사용, 정렬 키는 lambda식 사용
        pass

    def set_player(self):
        # 게임을 시작할 때 플레이어 아이디를 입력받는 함수
        self.cur_player= input("플레이어 아이디를 입력하세요: " )

        if not self.player_list.get(self.cur_player, None):
            print('신규플레이어초기화')
            self.player_list[self.cur_player] = 0

    def start_game(self):
        # 게임을 초기화 
        self.init_game()

        # 플레이어 세팅
        self.set_player()
        
        count = 0

        # 게임 루프
        # 게임이 끝날 때 까지 무한 반복
        # 루프 중 고려해야할 사항
        # 1. 사용자 입력 유효성 검사, 3자리 숫자인지, 숫자인지
        # 2. 플레이어가 정답을 맞히면 self.palyer_list에 점수를 저장하고 루프를 탈출
        #    점수를 저장할 때 기존 점수보다 더 좋은 점수일 경우에만 저장
    
        while True:
            number_game_userlist = []
            number_game_user = input("3자리수를 입력해주세요 :")

            if number_game_user.isdigit() == True :
                digit3.q(number_game_user)
                if len(number_game_user) != 3 :
                    print("3자리 숫자를 입력해주세요.")
                else:
                    for i in range(0,3):
                        number_game_userlist.append(int(number_game_user[i]))                    
                    count +=1
                    print(digit3.q(number_game_userlist))
                    if digit3.q(number_game_userlist).get('strike') ==3 :
                        if digit3.player_list[self.cur_player] == 0 : 
                            digit3.player_list[self.cur_player] = count
                        
                        elif digit3.player_list[self.cur_player] >= count :
                            digit3.player_list[self.cur_player] = count
                        else :
                            digit3.player_list[self.cur_player] = digit3.player_list[self.cur_player]
                        print(digit3.player_list)
                        break
                        
            else :
                print("3자리 숫자를 입력해주세요.")     

    

if __name__ == '__main__':
    # 게임 객체를 생성
    digit3 = Digit3()
    digit3.start_game()
    # 플레이어의 성적을 화면에 뿌림
    digit3.rank()




