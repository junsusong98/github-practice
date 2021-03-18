# 2017014584 송준수
import numpy as np
a1 = np.full((3,3),2)  # all values is 2, (3,3)matrix
a2 = np.arange(1,13)   # list [1,2,3,4,5,6,7,8,9,10,11,12] ,1D matrix, (12,)
a3 = np.arange(3,50,3)  # list [ 3  6  9 12 15 18 21 24 27 30 33 36 39 42 45 48], 1D matrix step =3
a4 = np.linspace(0,20,5)  # (start,end, number) linspace mean liner spaaced values

print("a1 =",a1)
print("a2 =",a2)
print("a3 =",a3)
print("a4 =",a4)

