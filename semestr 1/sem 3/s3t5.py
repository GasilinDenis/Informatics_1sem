import numpy as np
n=int(input()) #Кол-во строк
m=int(input()) #Кол-во столбцов
mat=np.zeros((n,m),dtype=int)
x=1
top, bot = 0, n-1                                       # [ ---> - top - --|--]
left, right = 0, m-1                                    # [ left - --- - right]
while top<=bot and left<=right:                         # [ --|- - bot - <----]
    for i in range(left,right+1): # -->
        mat[top][i]=x
        x+=1
    top+=1
    for i in range(top,bot+1): # down
        mat[i][right]=x
        x+=1
    right-=1
    if top<=bot:
        for i in range(right,left-1,-1): # <--
            mat[bot][i]=x
            x+=1
        bot -= 1
    if left<=right:
        for i in range(bot,top-1,-1): # up
            mat[i][left]=x
            x+=1
        left+=1

print(mat)

