# for문을 사용해서 코드를 짤 수 있다.

result = 1 
# 변수 result의 초기값을 1로 설정한다.                               
for i in range(1, 11):                  
# 1부터 10까지 의 값을 i 에 차례대로 대입한다.
    result = result * i                 
    ''' (오른쪽 result) 초기값 1 에 i를 곱한 값이 왼쪽 result에 대입된다.                                 
        i 가 10이 될 때까지 계속 result값에 곱이 가해지며 result 값이 변한다.'''
print(result)                           
# result에 1 * 1 * 2 * 3 * ...*10 값이 담기게 되고 그 값을 출력한다.