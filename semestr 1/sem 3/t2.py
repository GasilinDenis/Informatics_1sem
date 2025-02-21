n=int(input())
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
print(f)
