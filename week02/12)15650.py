# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. 

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.


import sys
from itertools import combinations  # 조합을 구하기 위한 라이브러리 사용

# 입력 받기
n, m = map(int, sys.stdin.readline().split())

# 1부터 N까지의 수 중에서 M개를 선택하는 모든 조합 출력
for combo in combinations(range(1, n + 1), m):
    print(" ".join(map(str, combo)))
