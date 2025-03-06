N, M = map(int, input().split())

s = []

def dfs():
    if len(s) == M: #M개의 숫자를 선택했으면 출력력
        print(' '.join(map(str,s)))
        return #백트래킹: 더이상 진행 않고 돌아감감
    for i in range(1,N+1): # 1부터 N 까지 숫자를 확인인
        if i not in s: #중복 방지
            s.append(i) #s 에 i를 추가한다다
            dfs() # 다음 숫자 선택을 위해 재귀 호출출
            s.pop() #백트래킹: 선택한 숫자 제거 및 이전 상태로 복구구
dfs() #탐색 시작작