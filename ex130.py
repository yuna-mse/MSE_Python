import requests                                                                 
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# btc에는 딕셔너리 형태로 담긴 비트코인의 정보들이 대입된다.
     
# 변수 btc에 담긴 값들을 이용해 변동폭, 시가, 최고가의 코드를 작성한다. 
변동폭 = float(btc['max_price']) - float(btc['min_price'])
''' btc의 max_price에 해당하는 value와 min_price에 해당하는 value를 float함수를 사용해 실수로 만들어주고 빼준다. 
    그 값을 변수 변동폭에 대입한다.'''                         
시가 = float(btc['opening_price'])
# btc의 opening_price에 해당하는 value값을 float 함수를 사용해 실수로 변환하고 그 값을 변수 시가에 대입한다.                                           
최고가 = float(btc['max_price'])
# btc의 max_price에 해당하는 value값을 float함수를 사용해 실수로 만들어주고 그 값을 변수 최고가에 대입한다.
''' max_price, min_price, opening_price의 value들은 문자열로 표현되므로 연산이 불가능하다.                           
    따라서 float 함수를 이용해 문자열을 실수로 바꿔준다.'''

if (시가 + 변동폭) > 최고가:    #(시가 + 변동폭)이 최고가보다 크면
    print("상승장")         #상승장을 출력하고
else:                     # 아니라면
    print("하락장")         # 하락장을 출력한다.   
    