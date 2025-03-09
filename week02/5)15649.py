# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

#백트래킹 이용해서 풀기
import sys

N, M = map(int, sys.stdin.readline().split())
visited = [False] * (N + 1)  # 방문 여부 체크 리스트
result = []  # 현재 선택된 숫자들을 저장할 리스트

def backtrack():
    if len(result) == M:  # M개의 숫자를 선택하면 출력
        print(" ".join(map(str, result)))
        return
    
    for i in range(1, N + 1):
        if not visited[i]:  # 아직 선택되지 않은 숫자라면
            visited[i] = True  # 방문 체크
            result.append(i)  # 숫자 추가
            backtrack()  # 재귀 호출 (다음 숫자 선택)
            result.pop()  # 백트래킹 (되돌리기)
            visited[i] = False  # 방문 해제

backtrack()