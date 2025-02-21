n = int(input())
A= [1,2]
for i in range(2,n):
    A.append(A[i-1]+A[i-2])
print(A[n-2])