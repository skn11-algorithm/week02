# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# # N이 커질수록 판별 해야하는 값도 많아지기때문에 일반적인 방법으로 소수를 판별할 경우 너무 느림
# # >> 따라서 '에라토스테네스의 체'알고리즘을 사용하면 간편하고 빠르다!
# # 소수의 배수를 전부 제거하는 원리

import sys

M, N = map(int, sys.stdin.readline().split())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # √N 판별법!!
        if n % i == 0:
            return False
    return True

for num in range(M, N + 1):
    if is_prime(num):  # 소수라면 출력되게
        print(num)
