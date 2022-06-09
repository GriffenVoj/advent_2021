from collections import Counter 


data=open("data.txt").read()
data=data.split(",")

def set_up(start_con):
    r=Counter()
    for i in range(9):
        r[i]=0
    for item in start_con:
        r[int(item)]+=1
    return r

def run(days):
    r=Counter()
    for i in range(9):
        r[i]=0
    fish=set_up(data)
    print(fish  )
    for i in range(days):
        for x in range(8,-1,-1):
            if x==0:
                r[8]+=fish[x]
                r[6]+=fish[x]
            else:
                r[x-1]+=fish[x]
        fish=r.copy()
        r=Counter()   
    return sum(fish.values())

#part 1 answer
print("pt1",run(80), "pt2",run(256))
