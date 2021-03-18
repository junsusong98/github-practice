# 2017014584 송준수
import numpy as np

a = np.array([[1,1,-1],[2,-1,3],[1,2,1]])
# x + y - z = 0    [1, 1,-1][x]   [0]
# 2x - y + 3z = 9  [2,-1, 3][y] = [9]
# x + 2y + z = 8   [1, 2, 1][z]   [8]
b = np.array([0,9,8])

c = np.linalg.solve(a,b)
# c = [1,2,3]
print("x={}, y={}, z={}".format(c[0],c[1],c[2]))