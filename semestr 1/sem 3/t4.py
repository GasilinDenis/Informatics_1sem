x=int(input())
s=str(input())
for i in range(1,((x+1)//2)+1):
    print(s*i)
if x % 2 == 0:
    for i in range(((x+1)//2), 0, -1):
        print(s * i)
else:
    for i in range(((x+1)//2) - 1, 0, -1):
        print(s * i)
