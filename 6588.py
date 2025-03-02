# n = int(input())
# # n = a + b
# # b-a가 가장 큰 것을 출력
# # 불가능할 시 Goldbach's conjecture is wrong. 출력
# # 0 입력시 종료

# for i in range(3, n, -1):
#     if n == 0:
#         break
#     for j in range(3, int(i**0.5)+1):
#         if i % j != 0:
            

# https://changha-dev.tistory.com/181 참고하였음

import math
import sys 

# 에라토스테네스의 체 == 주어진 범위 내의 소수 리스트 반환하는 효율적인 알고리즘 
def sieve_of_eratosthenes(n):
    prime = [True for _ in range(n+1)]
    prime[0] = prime[1] = False # 0과 1 제외
    for i in range(2, int(math.sqrt(n)) + 1):
        if prime[i] == True:
            for j in range(i*i, n+1, i):
                prime[j] = False #i의 배수를 모두 False로 만듦
    return prime

max_n = 1000000
prime_list = sieve_of_eratosthenes(max_n)

while True:
    n = int(sys.stdin.readline()) # 시간초과 방지
    if n == 0:
        break
	# 홀수만 찾으면 되므로 2씩 더해준다.
    for i in range(3, int(n/2)+1, 2): 
        if prime_list[i] and prime_list[n-i]: #리스트에서 두 홀수 값이 소수인 경우
            print(f"{n} = {i} + {n-i}")
            break

    else:
        print("Goldbach's conjecture is wrong.")