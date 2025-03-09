# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

n = int(input()) # 1. 소수 몇개 입력할건지
numbers = list(map(int, input().split())) # 2. 직접 소수 입력  --> map은 일회성 iterator이므로 여러번 반복문에 추가하기 위해서는 list 형태로 감싸주어야한다. 
result = 0 # 결과값 초기화 

for number in numbers:
    if number == 1: # 1은 소수가 아님을 먼저 거르고
        continue
    
    prime = True # 소수를 판별하기 위한 bool 변수를 지정 
    for i in range(2, int(number ** 0.5) + 1): # 소수 판별하는 루프
         if number % i == 0 : # if : number 전의 수로 나눈 결과 나눠진다? 
             prime = False  # then : 소수가 아니다!!
             break 
    else:
        result += 1 # 소수 개수 하나씩 추가하기 

print(result)

'''       
* 소수 찾기에서 제곱근을 사용하는 이유
    - 어떤 숫자가 합성수라면, 약수 두개의 곱으로 표현할 수 있다
    - a * b = 36 이라고 치면 1*36 / 2*18 / 3*12 / 4*9 / 6*6으로 표현
    - 이후 큰 수는 36*1 이런식으로 반복되므로 
    - a b 둘 중 반드시 하나는 제곱근 number이다.
    - 따라서 2~제곱근 num을 쓰면 소수의 판별 범위를 지정할 수 있다 

'''