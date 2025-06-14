import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
d = [[False for _ in range(n)] for _ in range(n)]
for _ in range(m):
  i,j = map(int,input().split())
  d[i-1][j-1] = True
  d[j-1][i-1] = True

next = set()
virus = [0 for _ in range(n)]
virus[0] = 1
for k in range(n):
  if d[0][k] == True:
    next.add(k)
    virus[k] = 1
while next:
  a = next.pop()
  for b in range(n):
    if d[a][b] == True:
      if virus[b] != 1:
        next.add(b)
        virus[b] = 1
print(sum(virus)-1)