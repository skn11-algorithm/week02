# 6001
print("Hello")

# 6002
print("Hello World")

# 6003
print("Hello\nWorld")

# 6004
print("'Hello'")

# 6005
print('"Hello World"')

# 6006
print('"!@#$%^&*()"')

# 6007
print('"C:\\Download\\\'hello\'.py"')

# 6008
print('print("Hello\\nWorld")')

# 6009
print(input())

# 6010
print(int(input()))

# 6011
print(float(input()))

# 6012
a = input()
b = input()
print(a)
print(b)

# 6013
a = input()
b = input()
print(b)
print(a)

# 6014
a = float(input())
print(a)
print(a)
print(a)

# 6015
a, b = map(int, input().split())
print(a)
print(b)

# 6016
a, b = input().split()
print(b, a)

# 6017
a = input()
print(a, a, a)

# 6018
h, m = input().split(":")
print(h, m, sep=":")

# 6019
y, m, d = input().split(".")
print(d, m, y, sep="-")

# 6020
a, b = input().split("-")
print(a, b, sep="")

# 6021
s = input()
for c in s:
    print(c)

# 6022
s = input()
print(s[:2], s[2:4], s[4:])

# 6023
h, m, s = input().split(":")
print(m)

# 6024
a, b = input().split()
print(a + b)

# 6025
a, b = map(int, input().split())
print(a + b)

# 6026
a = float(input())
b = float(input())
print(a + b)

# 6027
print(hex(int(input()))[2:])

# 6028
print(hex(int(input())).upper()[2:])

# 6029
print(int(input(), 16))

# 6030
print(ord(input()))

# 6031
print(chr(int(input())))

# 6032
print(-int(input()))

# 6033
print(chr(ord(input()) + 1))

# 6034
a, b = map(int, input().split())
print(a - b)

# 6035
a, b = map(float, input().split())
print(a * b)

# 6036
s, n = input().split()
print(s * int(n))

# 6037
n = int(input())
s = input()
print(s * n)

# 6038
a, b = map(int, input().split())
print(a ** b)

# 6039
a, b = map(float, input().split())
print(a ** b)

# 6040
a, b = map(int, input().split())
print(a // b)

# 6041
a, b = map(int, input().split())
print(a % b)

# 6042
print(round(float(input()), 2))

# 6043
a, b = map(float, input().split())
print(f"{a / b:.3f}")

# 6044
a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(f"{a / b:.2f}")

# 6045
a, b, c = map(int, input().split())
print(a + b + c, f"{(a + b + c) / 3:.2f}")

# 6046
print(int(input()) << 1)

# 6047
a, b = map(int, input().split())
print(a << b)

# 6048
a, b = map(int, input().split())
print(a < b)

# 6049
a, b = map(int, input().split())
print(a == b)

# 6050
a, b = map(int, input().split())
print(a <= b)

# 6051
a, b = map(int, input().split())
print(a != b)

# 6052
print(bool(int(input())))

# 6053
print(not bool(int(input())))

# 6054
a, b = map(int, input().split())
print(bool(a) and bool(b))

# 6055
a, b = map(int, input().split())
print(bool(a) or bool(b))

# 6056
a, b = map(int, input().split())
print(bool(a) ^ bool(b))

# 6057
a, b = map(int, input().split())
print(bool(a) == bool(b))

# 6058
a, b = map(int, input().split())
print(not (bool(a) or bool(b)))

# 6059
print(~int(input()))

# 6060
a, b = map(int, input().split())
print(a & b)

# 6061
a, b = map(int, input().split())
print(a | b)

# 6062
a, b = map(int, input().split())
print(a ^ b)

# 6063
a, b = map(int, input().split())
print(a if a > b else b)

# 6064
a, b, c = map(int, input().split())
print(min(a, b, c))

# 6065
a, b, c = map(int, input().split())
for num in (a, b, c):
    if num % 2 == 0:
        print(num)

# 6066
a, b, c = map(int, input().split())
for num in (a, b, c):
    print("even" if num % 2 == 0 else "odd")

# 6067
n = int(input())
if n < 0:
    print("A" if n % 2 == 0 else "B")
else:
    print("C" if n % 2 == 0 else "D")

# 6068
n = int(input())
if n >= 90:
    print("A")
elif n >= 70:
    print("B")
elif n >= 40:
    print("C")
else:
    print("D")

# 6069
grade = input()
print("best!!!" if grade == "A" else "good!!" if grade == "B" else "run!" if grade == "C" else "slowly~" if grade == "D" else "what?")

# 6070
season = int(input()) // 3
print("winter" if season == 1 or season == 4 else "spring" if season == 2 else "summer" if season == 3 else "fall")

# 6071
while (n := int(input())) != 0:
    print(n)

# 6072
n = int(input())
while n:
    print(n)
    n -= 1

# 6073
n = int(input())
while n:
    n -= 1
    print(n)

# 6074
c = ord(input())  # 입력받은 문자 ASCII 코드 변환
for i in range(97, c + 1):  # 'a'부터 입력 문자까지 출력
    print(chr(i), end=" ")

# 6075
n = int(input())
for i in range(n + 1):
    print(i)

# 6076
n = int(input())
for i in range(n + 1):
    print(i)

# 6077
n = int(input())
print(sum(i for i in range(n + 1) if i % 2 == 0))

# 6078
while (c := input()) != "q":
    print(c)
print("q")

# 6079
n, s = int(input()), 0
for i in range(1, n + 1):
    s += i
    if s >= n:
        print(i)
        break

# 6080
n, m = map(int, input().split())
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(i, j)

# 6081
n = int(input(), 16)
for i in range(1, 16):
    print(f"{n:X}*{i:X}={n*i:X}")

# 6082
n = int(input())
for i in range(1, n + 1):
    print("X" if any(c in str(i) for c in "369") else i, end=" ")

# 6083
r, g, b = map(int, input().split())
print(r * g * b)
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)

# 6084
h, b, c, s = map(int, input().split())
print(f"{(h * b * c * s) / 8 / 1024 / 1024:.1f} MB")

# 6085
w, h, b = map(int, input().split())
print(f"{(w * h * b) / 8 / 1024 / 1024:.2f} MB")

# 6086
n, s, i = int(input()), 0, 1
while s < n:
    s += i
    i += 1
print(s)

# 6087
n = int(input())
for i in range(1, n + 1):
    if i % 3 != 0:
        print(i, end=" ")

# 6088
a, d, n = map(int, input().split())
print(a + (n - 1) * d)

# 6089
a, r, n = map(int, input().split())
print(a * (r ** (n - 1)))

# 6090
a, m, d, n = map(int, input().split())
for _ in range(n - 1):
    a = a * m + d
print(a)

# 6091
a, b, c = map(int, input().split())
d = 1
while d % a or d % b or d % c:
    d += 1
print(d)

# 6092
n = int(input())
arr = [0] * 24
for i in map(int, input().split()):
    arr[i] += 1
print(*arr[1:])

# 6093
n = int(input())
arr = list(map(int, input().split()))
print(*arr[::-1])

# 6094
n = int(input())
print(min(map(int, input().split())))

# 6095
board = [[0] * 19 for _ in range(19)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1
for row in board:
    print(*row)

# 6096
board = [list(map(int, input().split())) for _ in range(19)]
n = int(input())
for _ in range(n):
    x, y = map(lambda v: int(v) - 1, input().split())
    for i in range(19):
        board[x][i] ^= 1
        board[i][y] ^= 1
for row in board:
    print(*row)

# 6097
h, w = map(int, input().split())
board = [[0] * w for _ in range(h)]
n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    x, y = x - 1, y - 1
    for i in range(l):
        board[x + i * d][y + i * (1 - d)] = 1
for row in board:
    print(*row)

# 6098
board = [list(map(int, input().split())) for _ in range(10)]
x, y = 1, 1
while True:
    if board[x][y] == 2:
        board[x][y] = 9
        break
    board[x][y] = 9
    if board[x][y + 1] != 1:
        y += 1
    elif board[x + 1][y] != 1:
        x += 1
    else:
        break
for row in board:
    print(*row)
