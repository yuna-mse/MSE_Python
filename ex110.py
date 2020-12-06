if True :
# if문이 참이기때문에 바로 밑 if문이 실행되고 끝부분 else는 실행되지 않는다.
    if False:     # if문은 거짓이다.
        print("1")
        print("2")
    else:
        print("3")
        # if 문이 거짓이므로 print("3")이 실행되어 3이 출력되는 결과를 얻는다.
else :
    print("4")
print("5")
# print("5")가 화면에 출력된다.

# >>> 따라서 화면에는 3, 5가 개행되어 출력된다. 
