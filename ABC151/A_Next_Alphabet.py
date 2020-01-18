C = input()
# アルファベット小文字リスト
c_l = [chr(i) for i in range(97, 97+26)]

for i in range(len(c_l)):
  if c_l[i] == C:
    print(c_l[i+1])