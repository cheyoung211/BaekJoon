import sys
input = sys.stdin.readline
m = int(input())
s = set()
for _ in range(m):
  cmd = input().split()
  op,num = cmd[0], cmd [-1]
  if op == 'all':
    s = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
  elif op == 'empty':
    s = set()
  elif op == 'add':
    s.add(num)
  elif op == 'remove':
    if num in s:
      s.remove(num)
  elif op == 'check':
    print(1 if num in s else 0)
  else:
    if num in s: s.remove(num)
    else: s.add(num)