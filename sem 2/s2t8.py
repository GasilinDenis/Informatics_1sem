n=int(input())
A = list(map(int, input().split()))
for i in range(0, len(A)):
    less = 0
    equal = 0
    for k in range(0, len(A)):
        if A[k]>A[i]: less+=1
        elif A[k]==A[i]: equal+=1
    if less <= (n//2) < less+equal:
        print(A[i])
        break