# N개의 정수로 이루어진 수열이 있을 때, 
# 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

import sys

# 입력 받기
n, s = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

count = 0  # 조건을 만족하는 부분수열 개수 저장

# 백트래킹을 이용한 부분수열 탐색
def dfs(idx, total):
    global count
    if idx >= n:  # 배열의 끝까지 탐색 완료
        return
    
    total += numbers[idx]  # 현재 원소를 포함한 합 계산
    
    if total == s:  # 부분수열의 합이 S와 같다면 카운트 증가
        count += 1
    
    # 현재 원소를 포함하는 경우
    dfs(idx + 1, total)
    
    # 현재 원소를 포함하지 않는 경우
    dfs(idx + 1, total - numbers[idx])  # 다시 원래 상태로 복구

# DFS 탐색 시작
dfs(0, 0)

# 정답 출력
print(count)
