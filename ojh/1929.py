m,n=map(int,input().split())

# # 시간초과
# for i in range(m,n+1):
#     for j in range(2,i+1):
#         if i%j==0:
#             if j==i:
#                 print(j)
#             break



#에라토스테네스의 체
# 1. 2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다.
# 2. n의 최대 약수가 sqrt(n) 이하므로 i=sqrt(n) 까지 소수인지 검사
# 3. 소수가 발견되면 그 소수의 배수들을 제외

# 문제에서 m부터 n까지..
# sqrt(n)을 구함


m,n=map(int,input().split())
prime=[False,False]+[True]*(n-1) # 0 과 1 False 줘야함. 1이 입력될수도 잇음. 이거때매 틀렸었음

n_sqrt=int(n**0.5)

for i in range(2,n_sqrt+1):
    if prime[i]==True:
        for j in range(i+i,n+1,i): # 소수의 배수
            prime[j]=False

for i in range(m,n+1):
    if prime[i]:
        print(i)        
