A, B, K = map(int, input().split())
if A+B-K > 0:
  if A > K:
    print(A-K, B)
  else:
    print(0, B-(K-A))
  a = (A-K)
else:
  print(0, 0)