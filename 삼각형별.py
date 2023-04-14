def 삼각형_만들기(h):
    for i in range(1,h+1):
        알잘딱_함수('',h-i)
        알잘딱_함수('*',i)
        print()
def 알잘딱_함수(ch,n):
        print(ch*n,end='')
        #print(f'{ch*n:>{h}s}',end='')
        #for i in range(1,n+1):
        #    print(ch,end='')

h=int(input('높이를 입력하시오'))
삼각형_만들기(h)

