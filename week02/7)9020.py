# 1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 
# 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

# 골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 
# 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 
# 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 
# 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 
# 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
import sys

# 에라토스테네스의 체를 사용하여 10000 이하의 소수를 미리 계산
def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0과 1은 소수가 아님
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes

# 10000 이하의 모든 소수 미리 계산
prime_list = sieve(10000)

# 테스트 케이스 개수 입력
t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    
    # n을 두 개의 소수 합으로 표현하는 골드바흐 파티션 찾기
    a, b = n // 2, n // 2  # 중앙값부터 시작하여 차이가 가장 작은 쌍을 찾음
    
    while a > 0:
        if prime_list[a] and prime_list[b]:  # 두 수가 모두 소수인지 확인
            print(a, b)
            break
        a -= 1
        b += 1