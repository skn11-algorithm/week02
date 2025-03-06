M, N = map(int, input().split())

# 소수 판별 함수
def p(num): # 2보다 작은 수는 소수 아님
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: # 하나라도 나누어 떨어지면 소수가 아니다다
            return False
    return True

# M 이상 N 이하의 소수 출력
for num in range(M, N + 1):
    if p(num):
        print(num)
