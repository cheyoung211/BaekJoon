
import sys
input = sys.stdin.readline

def in_range(x,y,m,n):
  return 0 <= x and x < m and 0 <= y and y < n

t = int(input())
for _ in range(t):
  m,n,k = map(int,input().split())
  arr = [[0 for _ in range(n)] for _ in range(m)]
  for _ in range(k):
    x,y = map(int,input().split())
    arr[x][y] = 1
      
  cnt = 0
  visited = [[False for _ in range(n)] for _ in range(m)]
  next = []
  for a in range(m):
    for b in range(n):
      if visited[a][b] == False:
        visited[a][b] = True
        if arr[a][b] == 1:
          next.append((a,b+1))
          next.append((a+1,b))
          while next:
            x,y = next.pop()
            if in_range(x,y,m,n) and visited[x][y] == False:
              visited[x][y] = True
              if arr[x][y] == 1:
                if in_range(x,y+1,m,n) and visited[x][y+1] == False:
                  next.append((x,y+1))
                if in_range(x,y-1,m,n) and visited[x][y-1] == False:
                  next.append((x,y-1))
                if in_range(x+1,y,m,n) and visited[x+1][y] == False:
                  next.append((x+1,y))
                if in_range(x-1,y,m,n) and visited[x-1][y] == False:
                  next.append((x-1,y))
          cnt += 1
  print(cnt)