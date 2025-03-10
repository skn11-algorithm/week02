# question: 1부터 n까지 자연수 중 중복 없이 m개를 고른 수열 모두 구하기
# input: 자연수 n,m (1 ≤ M ≤ N ≤ 8)
# output: 1부터 n까지 자연수 중 중복 없이 m개를 고른 수열 모두
# idea: 결과값 저장할 배열 만들고, 백트래킹으로 1부터 n까지 돌면서 배열에 숫자가 없으면 배열에 더하기, 재귀함수로 호출하기, 트리 구조라 생각하면 편하겠군

arr = []
def backtracking():
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(1,n+1):
        if i not in arr:
            arr.append(i)
            backtracking()
            arr.pop()

n,m = list(map(int,input().split()))

backtracking()