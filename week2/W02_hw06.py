# 2017014584 송준수
import numpy as np
a = np.arange(0,16).reshape(4,4)
# Change "0 to 15" matrix back to the (4,4) matrix, 1D->2D

b= a[:,1]
# all row / second column
print("b =",b)

c= a[2,1:]
# Third row, second / Third,Fourth column
print("c =",c)

d=a[0:2,0:2]
# first,second row / first,second column
print("d =",d)

e=a[1:3,1:3]
# second,third row / second,third column
print("e =",e)