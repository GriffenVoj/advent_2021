data=open("realdata.txt").read().splitlines()
from collections import Counter

R=dict()
S=""
for i in data:
    if "-" in i:
        a,b=i.split(" -> ")
        R[a]=b
    else:
        S+=i
S_C=Counter()
print(S)
for i in range(len(S)-1):
    S_C[S[i]+S[i+1]]+=1

print(S_C)

for i in range(40):
    U_C=Counter()
    for k in S_C:
        U_C[k[0]+R[k]]+=S_C[k]
        U_C[R[k]+k[1]]+=S_C[k]
    S_C=U_C
L_C=Counter()
for l in S_C:
    L_C[l[0]]+=S_C[l]
L_C[S[-1]]+=1

print(L_C)
m=L_C.most_common()

print(m[0][1]-m[-1][1])
