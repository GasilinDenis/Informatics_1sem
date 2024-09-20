A = list(map(int, input().split()))
x=[]
for i in A:
    if A.count(i) == 1:
        x.append(i)
print(x)