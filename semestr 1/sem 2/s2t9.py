with open('file1.txt', 'r') as infile1:
    F1=infile1.readlines()
    x=0
    end=['.','!','...','?']
    for line in F1:
        A = list(line.strip())
        for i in range(0, len(A)):
            if (A[i] in end) and (A[i-1] not in end): x+=1
    print(x)
