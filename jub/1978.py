# 입력 받기
N = int(input())  # 숫자의 개수
numbers = list(map(int, input().split()))  # 숫자 리스트

# 소수 판별 함수
def p(num):
    if num < 2:  # 1은 소수가 아님
        return False
    for i in range(2, int(num ** 0.5) + 1):  # 2부터 √num까지 나눠보기
        if num % i == 0:
            return False
    return True

# 소수 개수 세기기
prime_count = sum(1 for num in numbers if p(num))

# 결과 출력
print(prime_count)

    