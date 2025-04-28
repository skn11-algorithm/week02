import itertools

a, b = map(int, input().split())

# lst = []
# for i in range(1, a + 1):
#     lst.append(i)



# 1. b개를 뽑는 법
# 
# 2. 가장 작은 순으로 나열하는 법
#   자연수로 만들어서 비교할 수 있을까




# ---
# python의 itertools 중 permutation 함수 사용

lsta = []
for i in range(1, a+1):
    lsta.append(i)

lst = list(itertools.permutations(lsta, b)) # 튜플 반환

for j in lst:
    print(*j) # 튜플 형식 없애기 위해 * 붙이기 


