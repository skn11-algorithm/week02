'''
코드 구글링
'''

# 자연수 n과 m이 주어졌을 때 아래 조건을 만족하는 길이가 m인 수열을 모두 구하는 프로그램을 작성하시오
# * 1부터 n까지 자연수 중에서 중복없이 m개를 고른 수열

n,m = list(map(int,input().split()))
 
s = []
 
def iter():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            iter()
            s.pop()
 
iter()