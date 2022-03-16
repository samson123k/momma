# N_C = int(input())
# N_list = []
# for i in range(0, N_C):
#     N = int(input())
#     N_list.append(N)

# N_list.sort()
# for i in N_list:
#     print(i)

from itertools import permutations

def F():
    for k in range(0,M):
        print(A[k], end = " ")
        if k == M-1:
            print("")
            

N, M = map(int, input().split(" "))
N_list = []
for i in range(1,N+1):
    user = i
    N_list.append(user)
N_list.sort()

S = list(permutations(N_list, M))
for i in range(0, len(S)):
    A = list(S[i])
    F()