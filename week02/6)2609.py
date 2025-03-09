# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

def gcd(a, b):
    for i in range(min(a, b), 0, -1):  # 큰 수부터 작은 수로 내려가며 찾기
        if a % i == 0 and b % i == 0:
            return i  # 최대공약수 반환