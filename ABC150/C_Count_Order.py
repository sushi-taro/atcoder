# 2020.1.10 ABC150 C
import math
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
m = math.factorial(N)
def calc_bango(lst):
  ban = 0
  for i in range(N):
    ban += lst[i]*math.factorial(N-i-1)  
  return(ban)

a = calc_bango(P)
b = calc_bango(Q)
print(abs(a-b))