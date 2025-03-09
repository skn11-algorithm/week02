# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

import sys

N = int(sys.stdin.readline()) 
numbers = list(map(int, sys.stdin.readline().split())) 

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # √N까지만 검사
        if n % i == 0:
            return False
    return True

count = 0

for num in numbers:
    if is_prime(num):  # 소수라면 count 증가되게
        count += 1

print(count)  
