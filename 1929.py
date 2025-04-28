# 범위 받기
min, max = map(int, input().split())

for i in range(min, max+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0: # 나누어 질 경우
            break   # 그 숫자는 패스
    else:# 살아남은 숫자는
        print(i)