import sys

def n_round(x):
  dec = x - int(x)
  if dec >= 0.5:
    return int(x) + 1
  else:
    return int(x)

n = int(sys.stdin.readline().rstrip())

if n == 0:
  print(0)
else:
  rates = sorted(int(sys.stdin.readline().rstrip()) for _ in range(n))
  extreme = n_round(n*0.15)
  middle_rates = rates[extreme:n-extreme]
  print(n_round(sum(middle_rates)/len(middle_rates)))