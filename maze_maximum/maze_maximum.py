import sys
import numpy as np
sys.stdin = open('./maze_maximum/input.txt', 'r')
sys.stdout = open('./maze_maximum/output.txt', 'w')
n, m = list(map(int, input().strip('').split(' ')))
mat = []
for i in range(n):
    row = list(map(int, input().strip('').split(' ')))
    mat.append(row)

arr = np.array(mat)
col_max = np.min(arr, axis=0)
max1 = np.max(col_max)
row_max = np.min(arr, axis=1)
max2 = np.max(row_max)
print(np.min([max1, max2]))
