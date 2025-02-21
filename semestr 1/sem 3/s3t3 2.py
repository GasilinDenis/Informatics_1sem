n = int(input())
m = int(input())

a, b = n, m
x0, y0 = 1, 0
x1, y1 = 0, 1

while b:
    q = a // b
    a, b = b, a % b
    x0, x1 = x1, x0 - q * x1
    y0, y1 = y1, y0 - q * y1

g = a
x = x0
y = y0

print(int(x), int(y), g)
