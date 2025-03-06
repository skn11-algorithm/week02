a,b = map(int,input().split())

# 최대 공약수:a,b를 모두 나눌 수 있는 약수 중 가장 큰 수수
#a,b중 가장 작은 숫자부터 1까지 -1 를 하면서 for 문 실행
#a와b를 i로 나눴을 때 나머지가 0이라면 i가 a,b의 최대 공약수수

for i in range(min(a,b),0,-1):
    if a%i == 0 and b%i ==0:
        print(i)
        break

# 최소 공배수: a,b의 배수들 중 공통 부분을 찾는 것
#a,b중 더 큰 수부터 a*b의 수 까지 for 문 실행
# 작은 수부터 하면 i가 ++1이 되면서 둘 중 큰 수에 도달 할 때까지 for문이 헛돌기 떄문
#j를 a,b로 나눴을 때 나머지 없으면 j는 a,b의 최소 공배수
for j in range(max(a,b),(a*b)+1):
    if j % a == 0 and j % b == 0 :
        print(j)
        break


