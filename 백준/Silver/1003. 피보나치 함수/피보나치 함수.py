import sys
input = sys.stdin.readline

memo = [0 for _ in range(41)]
memo[0] = (0,1)
memo[1] = (1,0)
def count(n,one, zero):
  if memo[n] != 0:
    return memo[n]
  else:
    if n == 1:
      one += 1
      return one,zero
    elif n == 0:
      zero += 1
      return one,zero
    else:
      one1,zero1 = count(n-1,one,zero)
      one2,zero2 = count(n-2,one,zero)
      memo[n] = (one1+one2, zero1+zero2)
      return one1+one2, zero1+zero2
    
t = int(input())
for _ in range(t):
  n = int(input())
  one, zero = count(n,0,0)
  print(zero, one)