"""
n,m=map(int,input().split())
big,small=(n,m) if n>m else (m,n)
gcd=1

big_lcm=[i for i in range(big,big*small+1,big)]
small_lcm=[i for i in range(small,big*small+1,small)]


for i in range(2,big+1):
    if n%i==0 and m%i==0:
        gcd=max(gcd,i)

print(gcd)
print(min(list(set(big_lcm)&set(small_lcm))))
"""


# 유클리드 호제법
# A를 B로 나누어 나머지 구함
# B,나머지를 다시 A,B로 생각하고 나머지가 0으로 될때까지 반복

# 24 18
# 18 6
# 6 0 -> 6이 최대공약수

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

# A= gcd * a
# B= gcd * b
# lcm=gcd*a*b
#     = A*B/gcd

n,m=map(int,input().split())
big,small=(n,m) if n>m else (m,n)
gcd=gcd(big,small)
lcm=(n*m)//gcd
print(gcd)
print(lcm)