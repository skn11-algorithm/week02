# 한 줄로 된 간단한 에디터를 구현하려고 한다. 이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 
# 최대 600,000글자까지 입력할 수 있다.

# 이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 문장의 맨 뒤(마지막 문자의 오른쪽), 
# 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다. 
# 즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.

# 이 편집기가 지원하는 명령어는 다음과 같다.

# L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
# 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $	$라는 문자를 커서 왼쪽에 추가함
# 초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어졌을 때,
# 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오. 
# 단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.

import sys

left_stack = list(sys.stdin.readline().strip())  # 커서 왼쪽 문자열을 저장하는 스택
right_stack = []  # 커서 오른쪽 문자열을 저장하는 스택
n = int(sys.stdin.readline().strip())  # 명령 개수 입력

for _ in range(n):
    command = sys.stdin.readline().strip().split()
    
    if command[0] == "L" and left_stack:
        right_stack.append(left_stack.pop())  # 커서를 왼쪽으로 이동
    elif command[0] == "D" and right_stack:
        left_stack.append(right_stack.pop())  # 커서를 오른쪽으로 이동
    elif command[0] == "B" and left_stack:
        left_stack.pop()  # 커서 왼쪽 문자 삭제
    elif command[0] == "P":
        left_stack.append(command[1])  # 커서 왼쪽에 문자 추가

# 최종 결과 출력 (left + reversed(right))
print("".join(left_stack + right_stack[::-1]))
