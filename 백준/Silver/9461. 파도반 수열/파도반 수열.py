import sys
input = sys.stdin.readline

p = [1,1,1,2,2,3,4,5,7,9]
for i in range(5,95):
  p.append(p[-1]+p[i])

t = int(input())
for _ in range(t):
  n = int(input())
  print(p[n-1])