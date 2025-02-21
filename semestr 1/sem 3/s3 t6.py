import numpy as np
x=np.array([1,2,3,4])
y=np.array([4,7,10,13])

#B[b0] = (x1.T[1 1 1 1] * x1 [1 1] ) ^ -1 * ([1 1 1 1] * [2])
# [b1]   (   [1 2 3 4]       [1 2] )        ([1 2 3 4]   [4])
#        (                   [1 3] )                     [6])
#        (                   [1 4] )                     [8])

def Lsq(x,y):
    x1= np.vstack((np.ones(len(x)), x)).T   #trans matrix with a row of 1 and X
    #print(x1)
    xtx=np.dot(x1.T, x1)      #mult of transp X1 and X1
    #print(xtx)
    xtx_inv=np.linalg.inv(xtx)     #outputs the inverted xtx matrix xtx*xtx_inv = E (1-matrix)
    #print(xtx_inv)
    xty=np.dot(x1.T,y)      #mult of transp x1 and y row
    #print(xty)
    B=np.dot(xtx_inv, xty)     #Matrix of b0 - intercept and b1 - slope
    return(B)
print(Lsq(x,y))