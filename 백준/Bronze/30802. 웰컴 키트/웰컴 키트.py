import math
n_people = int(input())
size_count = list(map(int,input().split()))
t,p = map(int,input().split())

print(sum([math.ceil(i/t) for i in size_count]))
print(n_people//p, n_people%p)