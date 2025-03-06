import math
import sys 

# 에라토스테네스의 체 == 주어진 범위 내의 소수 리스트 반환하는 효율적인 알고리즘 
def sieve_of_eratosthenes(n):
    prime = [True for _ in range(n+1)] #모든 수를 소수(True)로 가정한다
    prime[0] = prime[1] = False #0,1은 소수가 아님
    for i in range(2, int(math.sqrt(n)) + 1):
        if prime[i] == True: #if가 true 면 i는 소수
            for j in range(i*i, n+1, i): #i가 소수면 i의 배수들은 소수가 아님님
                prime[j] = False
    return prime

max_n = 1000000
prime_list = sieve_of_eratosthenes(max_n) #1~1000000까지의 소수 여부 저장장

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
	## 홀수만 찾으면 되므로 2씩 더해준다.
    for i in range(3, int(n/2)+1, 2): 
        if prime_list[i] and prime_list[n-i]:
            print(f"{n} = {i} + {n-i}")
            break

    else:
        print("Goldbach's conjecture is wrong.")