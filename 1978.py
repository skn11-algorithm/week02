# 갯수 받기
a = int(input())
# 숫자들 받기
b = list(map(int, input().split()))
# 카운트
count = 0

for i in b: # 리스트 내 숫자에 대해
    if i == 1:  # 1은 당연히 제외
        count += 1
        continue
    for j in range(2, i):
        if i % j == 0:  # 2부터 i까지 나누어 보아 나머지가 0인 경우 발생시
            count += 1 #count에 +1
            break  # 다음 숫자로
        
print(a-count) #전체 갯수 - 소수의 갯수

