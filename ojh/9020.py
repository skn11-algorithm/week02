import sys

def prime(n):
    n_sqrt=int(n**0.5)
    p=[False,False]+[True]*(n-1)
    for i in range(2,n_sqrt+1):
        if p[i]==True:
            for j in range(i*i,n+1,i): # 소수의 배수 #i*i부터 시작하면 이미 처리된 숫자는 건너뛸 수 있어서 효율적.
                p[j]=False
    return p

prime_arr=prime(10000)
n=int(sys.stdin.readline())

for _ in range(n):
    m=int(sys.stdin.readline())
    m_prime=[]
    for i in range(2,int(m/2)+1):
        if prime_arr[i] and prime_arr[m-i]: 
            m_prime.append((i,m-i))
    
    # 경우의 수 여러가지 -> 두 소수의 차이가 적은거
    if m_prime:
        print(m_prime[-1][0], m_prime[-1][1])
 
# m_prime에 i와 m-i 저장
# i는 작은 값부터 저장 중
# 제일 마지막에 저장되는 i는 제일 크고, m-i는 제일 작음
# 즉, 리스트의 마지막에 저장된 i와 m-i의 차이가 제일 적음