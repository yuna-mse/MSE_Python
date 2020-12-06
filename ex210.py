def message1():
    print("A")
    # message1()을 호출하면 A를 출력해라

def message2():
    print("B")
    # message2()를 호출하면 B를 출력해라

def message3():
#message3()을 호출하면
    for i in range (3) :
    # range(3)이 사용되었으므로 0부터 2까지의 값을 i에 차례로 대입하며 for문을 총 3번 돈다.  
        message2()
        # for문을 돌면서 message2()를 호출하고
        print("C")
        # c를 프린트한다.
    message1()
    # for문을 전부 돌고 난 후 message1()을 호출하여 A를 출력한다.

message3()
# >>> message3()을 구하기 위해 3번째 def 함수로 정의 한 for문 코드를 돈다.
# range(3)이 사용되었으므로 0부터 2까지의 값을 i에 차례로 대입하면서 for문을 총 3번 돈다.
# i가 0일 때 message2()를 호출해서 "B"를 프린트 하고 print("C")를 실행한다.
# i가 1일 때 다시 message2()를 호출하고 print("C")를 실행한다.
# i가 2일 때 다시 message2()를 호출하고 print("C")를 실행한다.
# for문을 전부 돌았으므로 다음 단계인 message1()을 호출하여 print("A")를 실행한다.

# 따라서 B C B C B C A 순으로 문자가 전부 개행되어 나오는 결과를 예상할 수 있다.