# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
n1, n2 = map(int, input().split())

'''
최대공약수
n1, n2 을 x로 나눳을 때 나머지가 0인 가장 큰 수

최소공배수 
n1, n2공통약수 다 곱하기

max = 0 
min = 0 # 일단 반환값 초기화

'''
# 공통약수 리스트 구하기
lst = []

for i in range(1, min(n1,n2)+1):
    if n1 % i == 0 and n2 % i == 0:
        lst.append(i)

print(max(lst)) #최대 공통 약수 (최대공약수)
print(max(lst) * (n1 // max(lst)) * (n2 // max(lst))) # 최대공약수를 제외한 n1, n2를 각각 max로 나눈 값을 모두 곱해줌
