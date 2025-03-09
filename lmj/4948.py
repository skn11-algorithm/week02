'''구글링 조금했어여 ㅠ'''
import sys, math

def d(N): # 소수를 찾는 함수
    if N == 1:
        return False
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True
    
sosu = [] # 소수를 담을 리스트 선언
for i in range(2, 2*123456): # 조건 범위안에 소수를 찾고 리스트에 추가
    if d(i):
        sosu.append(i)
        
while True:
    N = int(sys.stdin.readline()) # 입력이 여러개 일땐 sys 사용
    cnt = 0 # 갯수세기
    
    if N == 0: # 0이 입력되면 출력X
        break
        
    for i in sosu: # 소수 리스트안에 숫자를 하나씩 꺼내서 확인
        if N < i <= 2*N: # N보다 크고 2N보다 작거나 같으면 갯수 카운트 +1
            cnt += 1

    print(cnt)