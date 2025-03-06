import sys
li = {} #리스트

def p(num):
    if num in li: #이미 계산 값이면 바로 반환한다
        return li[num]
    
    if num < 2:
        li[num] = False

    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            li[num] = False
            return False
    li[num] = True
    return True

while True:
    n = int(sys.stdin.readline().strip())
    if n ==0:
        break

    count = sum(1 for num in range(n+1,2*n+1)if p(num))

    print(count)