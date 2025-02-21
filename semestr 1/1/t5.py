N,b,c = map(int, input().split())
N = str(N)
S = 0
p = len(N) - 1
for i in N:
    S += int(i) * (b**p)
    p -= 1
D = ''
while S > 0:
    D = str(S % c) + D
    S //= c
print(D)



