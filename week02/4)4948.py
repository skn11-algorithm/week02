# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 
# 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

import sys
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # √N까지만 검사
        if n % i == 0:
            return False
    return True

while True:
    n = int(sys.stdin.readline().strip()) 
    if n == 0:
        break  # 0이 입력되면 종료

    count = 0  # 소수 개수 카운트
    for num in range(n + 1, 2 * n + 1):  # n보다 크고 2n 이하의 숫자 탐색
        if is_prime(num): 
            count += 1

    print(count) 