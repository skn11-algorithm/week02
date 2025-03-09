# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

def prime_factorization(n):
    i = 2
    while i * i <= n:  # i가 sqrt(n)보다 작거나 같을 때까지만 확인
        while n % i == 0:  # i로 나누어 떨어지는 동안 반복
            print(i)
            n //= i
        i += 1  # 다음 숫자로 이동

    if n > 1:  # 마지막으로 남은 값이 1이 아니면 출력 (소수일 경우)
        print(n)

# 입력 받기
N = int(input())
if N > 1:
    prime_factorization(N)