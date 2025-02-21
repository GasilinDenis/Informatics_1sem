n=int(input())
m=int(input())
def prime(n):
    f=[]
    while n % 2 == 0:
        f.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            f.append(i)
            n //= i
    if n > 2:
        f.append(n)
    return f
a=prime(n)
b=prime(m)
d=[1]
for i in a:
    if i in b: d.append(i)
d.sort()
y=1.1
x=-2
while not y.is_integer():
    x += 1
    y = (1 - x * (n / d[-1])) / (m / d[-1])
print(int(x),int(y),d[-1])