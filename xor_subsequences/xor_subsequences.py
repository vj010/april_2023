import sys
import numpy as np
sys.stdin = open('./spe/input.txt', 'r')
sys.stdout = open('./xor_subsequences/output.txt', 'w')
n = int(input().strip())
arr = np.array(list(map(int, input().strip().split(' '))))
xors = set()
ans = []
for x in arr:
    tmp_set = set()
    for v in xors:
        new_xor = v ^ x
        if new_xor not in xors:
            tmp_set.add(new_xor)
    if x not in xors:
        xors.add(x)
    xors = xors.union(tmp_set)
    ans.append(len(xors))
print(' '.join(str(a) for a in ans))
