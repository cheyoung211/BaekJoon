import sys
input = sys.stdin.readline
n = int(input())

d = [0 for _ in range(10**6+1)]
d[1], d[2], d[3] = 0,1,1
for i in range(4,n+1):
  d[i] = d[i-1]+1
  if i%3 == 0:
    d[i] = min(d[i], d[i//3]+1)
  if i%2 == 0:
    d[i] = min(d[i], d[i//2]+1)

print(d[n])