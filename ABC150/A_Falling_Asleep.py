# 2020.1.11 dwango#6 A 
N = int(input())
lst = []
for _ in range(N):
  lst.append(list(input().split()))
X = input()
t = 0

for i,l in enumerate(lst):
  if l[0] == X:
    for j in range(i+1,N):
      t+=int(lst[j][1])

print(t)