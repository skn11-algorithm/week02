import sys

def prime(n):
    n_sqrt=int(n**0.5)
    p=[False,False]+[True]*(n-1)
    for i in range(2,n_sqrt+1):
        if p[i]==True:
            for j in range(i*i,n+1,i): # 소수의 배수 #i*i부터 시작하면 이미 처리된 숫자는 건너뛸 수 있어서 효율적.
                p[j]=False
    return p

prime_arr=prime(1000000)

while True:
    m=int(sys.stdin.readline())
    if m==0:
        break
    
    for i in range(3,m/2+1,2):
        if prime_arr[i] and prime_arr[m-i]: 
            print(m,"=",i,"+",m-i)
            break
    else: # for 루프가 break없이 끝난 경우 실행
        print("Goldbach's conjecture is wrong.")