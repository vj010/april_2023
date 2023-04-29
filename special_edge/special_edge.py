import sys
import numpy as np
import functools

sys.setrecursionlimit(100005)

time = 0


def dfs(node, visited, disc, subtree_sum, node_values, parent, low, total_sum, bridges):
    global time
    visited[node] = True
    time += 1
    disc[node] = low[node] = time
    subtree_sum[node] = node_values[node-1]
    for v in adj[node]:
        if not visited[v]:
            parent[v] = node
            dfs(v, visited, disc, subtree_sum, node_values,
                parent, low, total_sum, bridges)
            subtree_sum[node] += subtree_sum[v]
            low[node] = min(low[v], low[node])
            if low[v] > disc[node]:
                bridges.append(
                    (subtree_sum[v] * (total_sum-subtree_sum[v]),
                     min(node, v), max(node, v))
                )
        elif parent[node] != v:
            low[node] = min(low[node], disc[v])


def get_bridges(adj, node_values):
    print(len(node_values))
    disc = [np.Inf for i in range(len(adj))]
    low = [np.Inf for i in range(len(adj))]
    visited = [False for i in range(len(adj))]
    parent = [-1 for i in range(len(adj))]
    bridges = []
    subtree_sum = [0 for i in range(len(adj))]
    total_sum = np.sum(node_values)

    for i in range(1, len(adj)):
        # print(f"processing {i}")
        if not visited[i]:
            dfs(i, visited, disc, subtree_sum,
                node_values, parent, low, total_sum, bridges)
            pass
    return bridges


def custom_comparator(a, b):
    if a[0] < b[0]:
        return -1
    if a[0] == b[0] and a[1] < b[1]:
        return -1
    if a[0] == b[0] and a[1] == b[1] and a[2] < b[2]:
        return -1
    return 1


sys.stdin = open('./special_edge/input.txt', 'r')
sys.stdout = open('./special_edge/output.txt', 'w')
n, m = list(map(int, input().strip().split(' ')))
arr = np.array(list(map(int, input().strip().split(' '))))
adj = [[] for i in range(n+1)]
for i in range(m):
    u, v = list(map(int, input().strip().split(' ')))
    adj[u].append(v)
    adj[v].append(u)

bridges = get_bridges(adj=adj, node_values=arr)
if(len(bridges) == 0):
    print(f"{n+1} {n+1}")
    exit()
sorted_bridges = sorted(bridges, key=functools.cmp_to_key(custom_comparator))
print(f"{sorted_bridges[-1][1]} {sorted_bridges[-1][2]}")
