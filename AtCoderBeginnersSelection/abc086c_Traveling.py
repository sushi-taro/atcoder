N = int(input()) # Nは入力の回数
lst = []
# 入力t,x,yを取得
for i in range(N):
  t, x, y = map(int, input().split())
  lst.append([t, x, y])

def hantei(t,x,y,tn,xn,yn):
  tsub = abs(tn-t)
  xsub = abs(xn-x)
  ysub = abs(yn-y)
  if tsub%(xsub+ysub)==0:
    return True
  else:
    return False

t=x=y=0
tn=xn=yn=0
flg=True

if len(lst)==1:
    t=x=y=0
    tn = lst[0][0]
    xn = lst[0][1]
    yn = lst[0][2]
    if hantei(t,x,y,tn,xn,yn):
      pass
    else:
      flg = False
  
for i in range(len(lst)-1):
  if i == 0:
    t=x=y=0
    tn = lst[i+1][0]
    xn = lst[i+1][1]
    yn = lst[i+1][2]
    if hantei(t,x,y,tn,xn,yn):
      continue
    else:
      flg = False
      break
  else:
    t = lst[i][0]
    x = lst[i][1]
    y = lst[i][2]
    tn = lst[i+1][0]
    xn = lst[i+1][1]
    yn = lst[i+1][2]
    if hantei(t,x,y,tn,xn,yn):
      continue
    else:
      flg = False
      break
if flg:
  print('Yes')
else:
  print('No')