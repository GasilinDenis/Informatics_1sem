x = int(input())
A = list(input().strip())
s=str()
for i in range(0, len(A)-x+1,x):
    A[i:i + x] = A[i:i + x][::-1]
for i in A:
    s += i
print(s)
