#!/bin/python
from random import randint

def convert_to_tree(sequence):
    v = [[] for i in range(len(sequence) + 2)]
    degree = [1 for i in range(n + 2)]
    for i in sequence:
        degree[i] += 1

    for i in sequence:
        cur = 0
        while degree[cur] != 1:
            cur += 1
        v[cur].append(i)
        v[i].append(cur)
        degree[cur] -= 1
        degree[i] -= 1
    cur = 0
    while degree[cur] != 1:
        cur += 1
    a = cur
    cur += 1
    while degree[cur] != 1:
        cur += 1
    b = cur

    v[a].append(b)
    v[b].append(a)

    return v

n = 4
l = 0
r = 10
sequence = [randint(0, n - 1) for i in range(n - 2)]

v = convert_to_tree(sequence)

print(1)
print(n)
for i in range(n):
    a = randint(l, r)
    b = randint(a, r)
    print(a, b)


for num, i in enumerate(v):
    for j in i:
        if num < j:
            print(num + 1, j + 1)


