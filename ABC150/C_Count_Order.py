# 2020.1.10 ABC150 C
import itertools
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

def count_junretsu(retsu):
	# 大きさNの順列を辞書順に作成し、順番にP,Qと比較する
	for i,l in enumerate(itertools.permutations(range(1,N+1))):
		if retsu == list(l):
			return(i+1)

a = count_junretsu(P)
b = count_junretsu(Q)
print(abs(a-b))