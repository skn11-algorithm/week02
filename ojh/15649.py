def combi(d):
    # 반환 조건
    if d==m:
        print(" ".join(map(str, arr)))
        return
    
    for i in range(1,n+1):
        if chk[i]==False:
            chk[i]=True
            arr.append(i)
            combi(d+1)
            chk[i]=False
            arr.pop()

n,m=map(int,input().split())
arr=[]
chk=[False]*(n+1)
combi(0)

"""
def combi():
    # 반환 조건
    if len(arr)==m:
        #print(*arr)
        print(" ".join(map(str, arr)))
        return
    
    for i in range(1,n+1):
        if i not in arr:
            arr.append(i)
            combi()
            arr.pop()


arr=[]
n,m=map(int,input().split())
combi()
"""