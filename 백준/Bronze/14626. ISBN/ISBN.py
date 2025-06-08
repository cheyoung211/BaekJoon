isbn = list(input())
check = int(isbn[-1])
s = 0
for i in range(0,12,2):
  if isbn[i] == '*':
    missing = 1
  else:
    s += int(isbn[i])

for j in range(1,12,2):
  if isbn[j] == '*':
    missing = 3
  else:
    s += int(isbn[j])*3

for k in range(0,10):
  if ((s+k*missing)%10 + check)%10 == 0:
    print(k)
    break