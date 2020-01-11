# 2020.1.10 ABC150 B
N = int(input())
S = input()

counter = 0
for i in range(N):
  s = S[i:i+3]
  if s == "ABC":
    counter += 1
print(counter)