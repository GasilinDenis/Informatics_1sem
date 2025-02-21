with open('input','r')as f1, open('output.txt', 'w') as f2:
    l1=f1.readlines()
    A=list(map(int,l1[0].split()))
    s=1
    if l1[1] == '+':
        s=(sum(A))
    if l1[1] == '-':
        s=(A[0]-sum(A[1:]))
    if l1[1] == '*':
        for i in A:
            s *= i
    f2.write(str(s))