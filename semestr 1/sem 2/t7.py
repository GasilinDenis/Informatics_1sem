A = list(map(int, input().split()))
x=0
for i in A:
    if A.count(i) > x: x=A[i]
print(x)
