low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []                                            
# 변수를 생성해서 비어있는 리스트를 하나 만든다.
for i in range(len(low_prices)):                           
# low_price 리스트에 담긴 원소의 갯수 5를 i에 대입하는 for문을 작성한다.
    volatility.append(high_prices[i] - low_prices[i])      
    ''' 리스트 인덱싱을 이용해 각 자릿수의 ( high_prices- low_prices )들을 구하고
        append 메서드 함수를 사용해서 각 자릿수의 ( high_prices- low_prices )들을 리스트 volatility 에 추가한다.'''
print(volatility)
# 5개의 (최댓값 - 최솟값) 원소가 추가된 리스트를 출력한다. 