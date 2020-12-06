# range 함수로 지정하는 간격은 정수값만 가능하다.
# numpy 모듈의 arange 함수는 실수값도 간격으로 설정할 수 있다.

import numpy                             
# numpy 를 불러온다.
for i in numpy.arange(0, 5.0, 0.1):      
# for문과 numpy.arange 함수를 이용해 0부터 5.0 까지 +0.1만큼 증가하는 값을 i에 대입한다. 
    print(i)
    # i를 출력한다.