N,K,M = map(int, input().split())
A = map(int, input().split())
x = 0 # N科目目の目標点

x = M*N-(sum(A))
if x > K:
  print(-1)
elif x < 0:
  print(0)
elif x <= K:
  print(x)