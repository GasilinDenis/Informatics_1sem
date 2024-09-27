import numpy as np
n=int(input()) #Кол-во строк
m=int(input()) #Кол-во столбцов
mat=np.zeros((n,m),dtype=int)
for i in range(0,n):
    l=list(map(int, input().split()))
    mat[i]=l
M=np.copy(mat)
Df=(np.linalg.det(np.delete(mat,m-1,axis=1))) #НЕ должно быть 0, а то ломается
def dd(mat,g):
    mat=np.copy(M) #вернуть оригинальную матрицу
    for i in range(0,n):
        mat[i][g]=M[i][m-1]  # ввести столбец b на место g
    mat=np.delete(mat,m-1,axis=1)
    d=np.linalg.det(mat)
    return d
for g in range (0,n): #перебрать все столбцы
    d=dd(mat,g)
    print(round(d/Df))
