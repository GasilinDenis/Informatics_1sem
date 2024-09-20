A = input().split(' ')
for i in range(0, len(A)-1, 1):
    A[0:len(A)-1], A[len(A)-1:len(A)] = A[len(A)-1:len(A)], A[0:len(A)-1]
print(A)