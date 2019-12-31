import re
S = input()

S = re.sub('eraser', '', S)
S = re.sub('erase', '', S)
S = re.sub('dreamer', '', S)
S = re.sub('dream', '', S)

if (len(S)==0):
  print('YES')
else:
  print(S)