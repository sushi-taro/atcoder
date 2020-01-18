N,M = map(int, input().split())

ans = {}
if M > 0:
  for _ in range(M):
    key, value = input().split()
    if key not in ans:
      ans[key] = []
    ans[key].append(value)
else:
  print(0," ",0)
  exit()

ac = 0
wa = 0

for v in ans.values():
  if 'AC' in v: # ACを出している場合
    for a in v:
      if a == 'WA':
        wa += 1
      else:
        ac += 1
        break
  else: # ACを出していない場合
    continue

print(ac, " ", wa)