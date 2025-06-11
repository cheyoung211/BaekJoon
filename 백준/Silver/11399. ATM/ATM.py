import sys
input = sys.stdin.readline
n = int(input())
time = list(map(int,input().split()))
time.sort()
weighted = [time[0]]
for i in time[1:]:
  t = weighted[-1] + i
  weighted.append(t)
print(sum(weighted))