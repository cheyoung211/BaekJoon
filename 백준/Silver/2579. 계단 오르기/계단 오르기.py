import sys
input = sys.stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]

d = [[0,0] for _ in range(n)]
d[0] = [s[0],0]
if n == 1:
    print(s[0])
else:
  d[1] = [s[0]+s[1],s[1]]
  for i in range(2,n):
    #마지막 이동: 1칸
    d[i][0] = d[i-1][1]+s[i]
    #마지막 이동: 2칸
    d[i][1] = max(d[i-2][0],d[i-2][1])+s[i]
  print(max(d[n-1]))