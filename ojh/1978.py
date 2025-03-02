import sys
input=sys.stdin.readline
n=int(input())
count=0
num_list=list(map(int,input().split()))

print(num_list)
for i in range(n):
    is_prime=True
    if num_list[i]>2:
        for j in range(2,num_list[i]):
            if num_list[i]%j==0:
                is_prime=False
                
    elif num_list[i]==2:
        is_prime=True
    else:
        is_prime=False
        
    if is_prime:
        count+=1
        
# for i in range(n):
#     for j in range(2,num_list[i]+1):
#         if num_list[i]%j==0:
#             if j==num_list[i]:
#                 count+=1
#             break


print(count)
