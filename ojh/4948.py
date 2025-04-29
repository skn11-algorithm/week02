prime=[False,False]+[True]*(123456*2-1)
n_sqrt=int((123456*2)**0.5)
for i in range(2,n_sqrt+1):
    if prime[i]==True:
        for j in range(i+i,(123456*2)+1,i): # 소수의 배수
            prime[j]=False

while True:
    n=int(input())
    if n == 0:
        break
    count=0
    for i in range(n+1,2*n+1):
        if prime[i]:
            count+=1
    print(count)