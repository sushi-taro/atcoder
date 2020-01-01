X = int(input())

while True:
  if X==2:
    break # Xが2の場合素数なのでwhileのループを抜ける
  for n in range(2, X):
    if X%n==0: # 2以上x未満の自然数nでxを割り切れるものが存在したのでxは素数ではない
      X+=1
      break # 一度forループを抜けて次のX+1を素数判定する 
  if n==X-1:
    break # 2以上x未満のすべての自然数でｘを割り切れなかった場合whileのループを抜ける
print(X)