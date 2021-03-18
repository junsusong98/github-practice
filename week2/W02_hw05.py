# 2017014584 송준수
import numpy as np
#1)
x = np.random.randint(1,100,size = 15)
# 1 to 100, 15 random number become "x"
a = np.array(x).reshape(3,5)
# Change "x" matrix back to the (3,5) matrix
print("a =",a)

#2)
print("max of a (axis 0) :",a.max(axis=0))
# Compare the numbers in each row. the max of them all
print("min of a (axis 0) :",a.min(axis=0))
# Compare the numbers in each row. the min of them all
print("mean of a (axis 0) :",a.mean(axis=0))
# Compare the numbers in each row. the average of them all

#3)
print("max of a (axis 1) :",a.max(axis=1))
# Compare the numbers in each column. the max of them all
print("min of a (axis 1) :",a.min(axis=1))
# Compare the numbers in each column. the min of them all
print("mean of a (axis 1) :",a.mean(axis=1))
# Compare the numbers in each column. the average of them all