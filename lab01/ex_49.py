# ex_49.py 예금 계좌 클래스
# -BankAccount 예금계좌 클래스 생성
# 변수 : 예금주 owner , 잔고 balance를 가짐
# 메소드 
# 입금 deposit
# 출금 withdraw
# 잔액확인 get_balance

def banksystem():
    while True:
        input(F"1.계좌생성")


class BankAccount:
     
    def __init__(self, owner, balance):
        owner_list = {}
        self.owner = owner
        self.balance = balance
        self.password = input("password를 입력해주세요: ")
        owner_list[self.owner] = self.password
        print(f"{owner}님의 계좌가 잔액 {balance}원으로 개설되었습니다.")

    def deposit(self, amount):
        if amount >0 :
            self.balance += amount
            print(f"{amount}원이 입급되었습니다.")
        else:
            print("0보다 큰 금액을 입력하시오.")

    def withdraw(self, amount) :
        if amount > self.balance :
            print("출금 금액이 현재 잔액보다 많습니다.")
        elif amount <0 :
            print("0보다 큰 금액을 입력하시오.")
        else :
            self.balance -= amount
            print (f"{amount}원이 출금되었습니다.\n계좌의 현재 잔액은 {self.balance}원 입니다.")
    def get_balance(self):
        print(f"계좌의 현재 잔액은 {self.balance}원 입니다.")
    
    def change_PW(self):
        check_PW =input("현재패스워드를 입력해주세요.: ")
        if check_PW == self.password :
            new_PW =input("변경하실 패스워드를 입력해주세요.: ")
            self.password = new_PW
        else:
            print("패스워드가 일치하지 않습니다.")
    # def spend_balance(self,p1,p2)
    #     self.p1 = input("계좌 소유주 성명을 입력해주세요. :")
    #         if self.p1 == account :
            
    #         elif self.p1 == account


# 계좌생성
account = BankAccount("홍길동",10000)
account = BankAccount("성길동",10000)
# account.deposit(5000)
# account.get_balance()
# account.withdraw(3000)
# account.change_PW()
