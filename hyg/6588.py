# question: 백만 이하의 모든 짝수에 대해 추측을 검증하는 프로그램 작성 (4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있음)
# input: 짝수 정수 n
# output: n = a + b | Goldbach's conjecture is wrong.
# idea: 에라토스테네스의 체로 소수면 True 배열 만들고 for문 돌려서 True인지 확인

import sys
import math

MAX_NUMBER = 1000000

prime = [True for _ in range(MAX_NUMBER + 1)]
prime[0] = prime[1] = False

for i in range(2, int(math.sqrt(MAX_NUMBER) + 1)):
    if prime[i]:
        for j in range(i*i, MAX_NUMBER + 1, i):
            prime[j] = False

def goldbach(n):
    for i in range(2, n):
        if prime[i] and prime[n-i]: 
            return i,n-i
    return None, None

while True:
    n = int(sys.stdin.readline())
    if n==0:
        break
    
    a,b = goldbach(n)
    if a:
        print('%d = %d + %d' %(n,a,b))
    else:
        print('Goldbach\'s conjecture is wrong.')