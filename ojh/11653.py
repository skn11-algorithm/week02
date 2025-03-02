# n=int(input())
# start=2
# while n>1:
#     if n%start==0:
#         n=n//start
#         print(start)
#     else:
#         start+=1
    
n=int(input())
i=2
while n>1:
    while(n%i==0):
        n=n//i
        print(i)
    i+=1