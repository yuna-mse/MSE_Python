# 먼저 입금, 출금을 할 계좌를 생성해아한다.
import random
# 랜덤 계좌번호를 만들기 위해 random을 import 한다.

class Account:
    # Account 클래스를 생성한다.
    account_count = 0     # <== class variable .클래스 공간 안에 변수가 생성됨
    
    def __init__(self, name, balance):            # __init__로 객체를 생성할 때마다 자동으로 호출할 함수를 입력한다. 
        # 생성자 self에 입력받는 값은 예금주 이름, 잔고이다.
        self.deposit_count = 0
        self.deposit_log = []       #1
        self.withdraw_log = []      #2
        #1, #2 --> 객체가 생성될 때 비어있는 리스트를 생성한다.
        
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        # self가 가리키는 공간에 새로운 이름의 변수를 만들고 입력받은 값을 저장한다. 

        # 계좌번호는 3-2-6 자릿수로 랜덤생성한다.
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        # 생성된 정수 값을 문자열로 변경하고 zfill을 사용해 원하는 자릿수로 만들어준다.
        num1 = str(num1).zfill(3)     # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)     # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)     # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        # 생성된 계좌번호를 self가 가리키는 객체 공간에 accoun_number라는 변수를 만들고 바인딩한다.  
       
    
    # 객체에 접근할 필요가 없는 값들을 @classmethod를 사용해서 정해줄 수 있다.
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)      # Account.account_count과 같은 결과를 프린트한다.

    def deposit(self, amount):
        if amount >= 1:
        # amount가 1보다 크거나 같으면(입금을 하면) 
            self.deposit_log.append(amount)
            # 예금을 할 때마다 그 내역을 리스트로 저장한다
            self.balance += amount
            # self가 있는 공간에 잔고가 있는데 그 잔고에 amount값을 더해준 값이 잔고가 됨

    def withdraw(self, amount):
        if self.balance > amount:
        # amount(출금할 금액)이 잔고보다 작으면
            self.withdraw_log.append(amount)
            # 출금을 할 때마다 그 출금액 내역을 리스트로 저장한다
            self.balance -= amount
            # 잔고에 amount 를 뺀 값이 잔고가 됨( = 출금)

    def withdraw_history(self):
        for amount in self.withdraw_log:
        # 출금할 금액을 self.withdraw_log에서 amount에 대입한다 
            print(amount)
            # 출금한 금액을 리스트에서 가져와 출력한다.
            
    def deposit_history(self):
        for amount in self.deposit_log:
        # 입금할 금액을 self.withdraw_log에서 amount에 대입한다
            print(amount)
            # 입금한 금액을 리스트에서 가져와 출력한다.
    
k = Account("Kim", 1000)
# 김씨가 처음에 1000원이 담긴 계좌를 가지고있다.

# 입금내역
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()
# 입금내역을 출력한다.

# 출금내역
k.withdraw(100)
k.withdraw(200)
k.withdraw_history()
# 출금내역을 출력한다.