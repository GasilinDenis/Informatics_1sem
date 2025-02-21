A = list(map(int, input().split()))

for x in A:
    if A.count(x) > 1:
        while x in A:
            A.remove(x)
print(A)