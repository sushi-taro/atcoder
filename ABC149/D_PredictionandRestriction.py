N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
# Kを無視した勝ち手のリスト
kachite = []
for i in range(N):
  if T[i] == 'r':
    kachite.append('p')
  elif T[i] == 's':
    kachite.append('r')
  else:
    kachite.append('s')

# 勝ち手リストを頭から見ていき、jとj-Kの勝ち手が同じ場合は変更する
for j in range(N):
  if j-K>=0:
    if kachite[j]==kachite[j-K] and kachite[j-K]!='':
      #K回前の勝ち手が同じ(得点が同じ)、かつ、空文字ではない場合
      kachite[j] = '' # K回前、K回後のいずれでもない手を出したことにする
# 最終得点を出力
rpoint = kachite.count('r')*R
spoint = kachite.count('s')*S
ppoint = kachite.count('p')*P
print(rpoint+spoint+ppoint)