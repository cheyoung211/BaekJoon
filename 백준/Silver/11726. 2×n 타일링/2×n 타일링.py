import sys
input = sys.stdin.readline
n = int(input())
d = [0 for _ in range(1001)]
d[1] = 1
d[2] = 2
d[3] = 3
if n >= 4:
  for i in range(4,n+1):
    d[i] = 2*d[i-2] + d[i-3]
print(d[n]%10007)