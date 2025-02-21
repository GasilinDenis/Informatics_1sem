with open('input','r')as f1, open('output', 'w') as f2:
    l1=f1.readlines()
    A=list(map(int,l1[0].split()))
    s=0
    b = int(l1[2])
    S = 0
    for i in range(0,len(A)):
        S=0
        N = str(A[i])
        p = len(N) - 1
        for j in N:
            S += int(j) * (b ** p)
            p -= 1
        A[i] = int(S)
        print(S)
    print(A)
    if l1[1].strip() == '+':
        for i in A:
            s += i
    if l1[1].strip() == '-':
        s=A[0]
        for i in A:
            s -= i
    if l1[1].strip() == '*':
        s=1
        for i in A:
            s *= i
    print(s)
    D = ''
    while s > 0:
        D = str(s % b) + D
        s //= b
    f2.write(str(D))