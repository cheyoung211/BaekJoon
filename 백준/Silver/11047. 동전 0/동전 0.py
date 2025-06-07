n,k = map(int,input().split())
coins = []
for _ in range(n):
  coins.append(int(input()))

cnt = 0
for i in coins[::-1]:
  q = k//i 
  if q != 0 :
    cnt += q
    k %= i
print(cnt)