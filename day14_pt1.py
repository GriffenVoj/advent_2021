data=open("testdata.txt").read().splitlines()
import numpy as np
import collections
import cache
def par(data_1):
    dictionary=dict()
    start=""
    for i in data_1:
        if "-" in i:
            g=i.split("->")
            dictionary[g[0][:-1]]=g[1][1:]
        else:
            start+=i
    return start,dictionary
line,rules=par(data)

def inserter(index,insertion,starty):
    for i in range(len(insertion)):
        sub=starty[:index[i]]+insertion[i]
        starty=sub+starty[index[i]:]
        index+=1
    return starty 
@cache
def synth(start,rule,x):
    indexholder=[]
    insertholder=[]
    print(start,"\n")
    for i in range(len(start)):
        if i !=0 and start[i-1:i+1] in rules.keys():
            indexholder.append(int(i))
            insertholder.append(rules[start[i-1:i+1]])
    indexholder=np.array(indexholder)        
    new=inserter(indexholder,insertholder,start)
    if x<40:
        return synth(new,rules,x+1)
    else:
        return start



bigboy=synth(line,rules,0)
badboy=collections.Counter(bigboy)
badboy=min(badboy,key=badboy.get)
biggie=collections.Counter(bigboy)
biggie=max(biggie,key=biggie.get)


print(bigboy.count(biggie)-bigboy.count(badboy))








