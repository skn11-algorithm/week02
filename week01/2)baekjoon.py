# 2557
print("Hello World")

# 1000
a, b = map(int, input().split())
print(a + b)

# 2558
a = int(input())
b = int(input())
print(a + b)

# 10950
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a + b)

# 10951
import sys
for line in sys.stdin:
    try:
        a, b = map(int, line.split())
        print(a + b)
    except:
        break

# 10952
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)

# 10953
t = int(input())
for _ in range(t):
    a, b = map(int, input().split(","))
    print(a + b)

# 11021
t = int(input())
for i in range(1, t + 1):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a + b}")

# 11022
t = int(input())
for i in range(1, t + 1):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a} + {b} = {a + b}")

# 11718
import sys
print(sys.stdin.read())

# 11719
import sys
print(sys.stdin.read())

# 11720
n = int(input())
print(sum(map(int, input())))

# 11721
s = input()
for i in range(0, len(s), 10):
    print(s[i:i+10])

# 2741
n = int(input())
for i in range(1, n + 1):
    print(i)

# 2742
n = int(input())
for i in range(n, 0, -1):
    print(i)

# 2739
n = int(input())
for i in range(1, 10):
    print(f"{n} * {i} = {n * i}")

# 1924
m, d = map(int, input().split())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekdays = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
print(weekdays[(sum(days[:m-1]) + d) % 7])

# 8393
n = int(input())
print(sum(range(1, n + 1)))

# 10818
n = int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums))

# 2438
n = int(input())
for i in range(1, n + 1):
    print("*" * i)

# 2439
n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

# 2440
n = int(input())
for i in range(n, 0, -1):
    print("*" * i)

# 2441
n = int(input())
for i in range(n):
    print(" " * i + "*" * (n - i))

# 2442
n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# 2445
n = int(input())
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# 2446
n = int(input())
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(2, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# 2522
n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * i)

# 10991
n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

# 10992
n = int(input())
print(" " * (n - 1) + "*")
for i in range(1, n - 1):
    print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")
if n > 1:
    print("*" * (2 * n - 1))
