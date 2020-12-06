per = ["10.31", "", "8.00"]

for i in per:
# per의 원소를 i에 차례대로 대입한다.
    try:
        print(float(i))
        # per의 각 문자열 원소를 실수로 변환하여 프린트 하라는 실행코드
    except:
        print(0)
        # 두번째 원소인 비어있는 문자열은 실수로 변환될 수 없어 예외가 발생하고, 그때 출력할 값인 0을 정하는 실행코드
    else:
        print("clean data")
        # 예외 없이 문자열이 실수로 변환되었을 때 clean data를 출력하는 실행코드
    finally:
        print("변환 완료")
        # 예외발생 유무에 상관 없이 "변환 완료" 를 출력하는 실행코드