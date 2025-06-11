import sys
L = int(sys.stdin.readline().strip())
string = sys.stdin.readline().strip()
s = 0
for idx,i in enumerate(string):
    a = ord(i) - 96
    s += a*(31**idx)
print(s%1234567891)