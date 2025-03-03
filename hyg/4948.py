# 베르트랑 공준: 임의의 자연수 n에 대해 n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 명제

# input: 여러 개의 n(자연수)
# output: n < x <= 2n인 x의 소수의 개수 구하기

# 생각 흐름: is_prime 함수 만들어서 소수면 true 반환 -> O(n^2) 시간이 소요될 것 같음 
# -> 시간을 줄일 수 있는 방법이 없을까 -> arr에 소수면 True 저장해놓기
# -> 소수에 true를 해놓고 for in range(n+1, 2n+1)까지 돌면서 true 개수 세기

# data structure: 1차원 array
# TC: O(n)
# SC: 1

import math

MAX_NUMBER = 123456*2

# 소수면 true인 배열 만들기
arr = [True for _ in range(0,MAX_NUMBER + 1)]

arr[0] = arr[1] = False

for i in range(2, int(math.sqrt(MAX_NUMBER)) + 1):  
    if arr[i]: 
        for j in range(i * i, MAX_NUMBER + 1, i):  # i의 배수들을 모두 제거
            arr[j] = False

# 소수의 개수 출력하기
while True:
    n = int(input())
    if n == 0:
        break
    
    print(sum(arr[n+1:2*n+1])) 
    
    
    
    
    