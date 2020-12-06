리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for i in 리스트:                                        
# for 문을 사용하여 리스트 안의 원소를 하나씩 i에 대입한다.
    name, ext = i.split('.')
    # i에는 문자열이 대입되므로 split()메서드를 사용해 i에 대입한 원소들을 . 을 기점으로 name과 ext로 각각 분리한다. 
    if ext == 'h' or ext == 'c':
    # 논리연산자 or을 사용. 만약 ext가 h 또는 c라면 
        print(i)
        # i를 출력한다.