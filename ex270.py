class Stock:
    pass
# 클래스 안에 아무것도 없는 객체를 생성한다.

class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
    # 생성자 self를 만들고 name, code, per, pbr의 값을 받는다.
    # __init__로 객체를 생성할 때마다 자동으로 호출할 함수를 입력한다.
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률
        # self 라는 객체 공간 안에 넘어온 이름과 같은 이름의 변수를 각각 만들고 함수 바깥에서 넘어온 값을 대입한다.

    # 메소드 추가를 위해 들여쓰기를 한다.
    def set_name(self, name):
    # 어떤 객체에 있는 name을 바꿔야하는지 알려줌
        self.name = name
        # 새로운 name을 self 객체공간 안의 name에 대입한다.

    def set_code(self, code):
    # 어떤 객체에 있는 code를 바꿔야하는지 알려줌
        self.code = code
        # 새로운 code를 self 객체공간 안의 code에 대입한다.
        
    def set_name(self, per):
    # 어떤 객체에 있는 per를 바꿔야하는지 알려줌
        self.per = per
        # 새로운 per을 self 객체공간 안의 per에 대입한다.
        
    def set_name(self, pbr):
    # 어떤 객체에 있는 pbr을 바꿔야하는지 알려줌
        self.pbr = pbr
        # 새로운 pbr을 self 객체공간 안의 pbr에 대입한다.
        
    def set_name(self, 배당수익률):
    # 어떤 객체에 있는 배당수익률을 바꿔야하는지 알려줌

        self.배당수익률 = 배당수익률
        # 새로운 배당수익률을 self 객체공간 안의 배당수익률에 대입한다.

    def get_name(self):
    # get 메서드를 사용하여 self의 어느 객체의 값을 가져갈건지 정해준다.
        return self.name
        # self가 가리키는 공간의 name을 리턴함

    def get_code(self):
    # get 메서드를 사용하여 self의 어느 객체의 값을 가져갈건지 정해준다.
        return self.code
        # self가 가리키는 공간의 code를 리턴함

# 3종목에 대한 객체를 생성하고 이를 리스트에 저장하기 위해 빈 리스트를 하나 만든다.
종목 = []

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)
# stock 클래스의 객체들을 만든다.

# 이 객체들을 append 메서드를 사용하여 처음에 만든 빈 리스트에 추가한다.
종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
# i에 삼성, 현대차, LG전자 객체를 대입한다.
    print(i.code, i.per) 
    # 삼성, 현대차, LG전자의 code와 per 값을 출력한다.
    ''' i가 stock 클래스의 객체를 대입하기때문에
        i.code로 종목코드에 접근하고 i.per로 per에 접근할 수 있다.'''