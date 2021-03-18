# 2017014584 송준수
import numpy as np       # Make 'numpy' simple with 'np'
c= np.array(range(0,9))  # list = [0,1,2,3,4,5,6,7,8]
print (c.ndim)           # number odf array dimensions  so, 1
print (c.shape)          # Tuple of array dimensions   s0, (9,)
print (c.size)           # number of element           so.1*9 = 9
print (c.dtype)          # date-type                    so, int 32
print (c. itemsize)      # length of one array element on byte  so, 4
print (c.data)           # python buffer object pointing to the start of th array's data so,<memory at 0x00000161652E5C40>