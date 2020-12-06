# def 함수를 사용해서 세개의 숫자를 입력받는 print_max 함수를 정의한다.

def print_max(a, b, c):
# a, b, c 를 입력받는 함수를 정의한다.
    if a > b and a > c:                   
    # 논리연산자 and 를 사용했다. 
        print(a)                          
        # 만약 a가 b, c 보다 더 크면 a를 출력하고
    elif b > a and b > c:
        print(b)                          
        # b가 a, c 보다 크면 b를 출력하고
    elif c > a and c > b:
        print(c)                          
        # c가 a, b 보다 크면 c를 출력해라 라는 뜻의 코드를 if문과 논리연산자를 이용하여 짜준다.
 
# 코드 확인 
print_max(10, 2, 4)
print_max(2, 10, 4)
print_max(2, 4, 10)