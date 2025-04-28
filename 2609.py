a, b = map(int, input().split())

# 유클리드 호제법

a2 = a
b2 = b
while b != 0:
    a, b = b, a % b

print(a)
print(int(a2*b2/a))



# for i in range (1, a):
#     if a % i == 0 and b % i == 0:
#         print(i)
#         break

# for j in range(b, ):
#     if j % a == 0 and j % b == 0:
#         print(j)
#         break