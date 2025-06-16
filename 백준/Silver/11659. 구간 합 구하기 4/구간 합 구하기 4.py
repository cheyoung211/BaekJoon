import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = list(map(int,input().split()))
s = [0]
for a in A:
  s.append(s[-1]+a)
for _ in range(m):
  i,j = map(int,input().split())
  print(s[j]-s[i-1])