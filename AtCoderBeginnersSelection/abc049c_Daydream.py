# 入力を取得
S = input()

def hikaku(s):
  cnum = len(s)
  if cnum == 5:
    if s!='maerd' and s!='esare':
      return False
    else:
      return True
  if cnum == 6:
    if s!='resare':
      return False
    else:
      return True
  if cnum == 7:
    if s!='remaerd':
      return False
    else:
      return True

S_rev = S[::-1] # Sを逆順に並べた文字列を使う
s = '' # S_revから取り出した文字列
start_ind = 0 # S_revから取り出す文字列の開始インデックス 
flg = True # S==Tの判定フラグ

if len(S_rev) < 5: # inputが5文字未満だった場合S!=T
  flg = False

while start_ind+5 <= len(S_rev):
  ### 文字数が大きい順に比較していく(dreamer=>eraser=>dream,erase)
  s = S_rev[start_ind:start_ind+7]
  # 'dreamer'との比較
  if hikaku(s): # 一致した場合開始インデックスを更新しwhileの処理を最初から実行する
    start_ind += 7
    continue
  else: # 不一致の場合6文字取り出す
    s = S_rev[start_ind:start_ind+6]
    # 'eraser'との比較
    if hikaku(s): # 一致した場合
      start_ind += 6
      continue
    else: # 不一致の場合5文字取り出す
      s = S_rev[start_ind:start_ind+5]
      # 'dream''erase'との比較
      if hikaku(s): # 一致した場合
        start_ind += 5
        continue
      else: # 不一致の場合S!=Tなのでflgを更新してループを抜ける
        flg = False
        break
        
if flg:
  print('YES')
else:
  print('NO')