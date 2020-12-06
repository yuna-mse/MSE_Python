string = 'abcd'
#'abcd' 문자열을 담는 변수 string 이 있다.
string.replace('b', 'B')
'''replace 메서드를 사용해 'abcd'의 'b'를 'B'로 바꾸는 문자열을 새로 생성했는데
   이 새로 생긴 문자열을 무엇도 대입하고있지 않다.
   따라서 'aBcd'는 메모리에 잠깐 저장되고 사라진다.''' 
print(string)
#string을 프린트한다.
#print(string)을 하면 'abcd'가 출력된다.