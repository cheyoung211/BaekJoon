eq = input()
s = []
num = ''
operand = 0
for i in eq:
  if i == '-':
    operand += int(num)
    s.append(operand)
    s.append(i)
    operand = 0
    num = ''
  elif i == '+':
    operand += int(num)
    num = ''
  else:
    num += i

if num != '':
  operand += int(num)
if operand != 0:
  s.append(operand)
result = s[0]

for j in s[1:]:
  if j != '-':
    result -= j
print(result)