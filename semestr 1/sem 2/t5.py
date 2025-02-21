A = input().split(' ')
A[0:len(A)-1], A[len(A)-1:len(A)] = A[len(A)-1:len(A)], A[0:len(A)-1]
print(A)