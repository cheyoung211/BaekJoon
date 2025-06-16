import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    items = defaultdict(set)
    for _ in range(n):
        item, category = input().split()
        items[category].add(item)
    c = 1
    for v in items.values():
        c *= (len(v)+1)
    print(c-1)