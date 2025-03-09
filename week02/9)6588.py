# 1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.
# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
# 예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 
# 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.

# 이 추측은 아직도 해결되지 않은 문제이다.
# 백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

import sys

# 에라토스테네스의 체를 이용하여 백만 이하의 소수를 미리 계산
def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0과 1은 소수가 아님
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes

# 1,000,000 이하의 모든 소수 미리 계산
limit = 1000000
prime_list = sieve(limit)

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break  # 0이 입력되면 종료

    found = False  # 골드바흐 파티션을 찾았는지 여부

    for a in range(3, n // 2 + 1, 2):  # 홀수 소수만 고려 (3부터 시작, 2씩 증가)
        b = n - a  # a + b = n을 만족하는 b 계산
        if prime_list[a] and prime_list[b]:  # 두 수가 모두 소수인지 확인
            print(f"{n} = {a} + {b}")
            found = True
            break  # 가장 작은 a를 찾으면 종료

    if not found:
        print("Goldbach's conjecture is wrong.")  # 골드바흐의 추측이 틀렸을 경우
