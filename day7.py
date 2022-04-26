data=open("data.txt").read().split(",")

import statistics

def blah(x):
    sub=[]
    for item in x:
        sub.append(int(item))
    fuel=0
    for item in x:
        fuel+=abs(int(item)-statistics.median(sub))
    return fuel

import math

def bleh(x):
    sub=[]
    for item in x:
        sub.append(int(item))
    steps=0
    fuel1=0
    for item in x:
        steps=abs(int(item)-math.floor(statistics.mean(sub)))
        fuel1+=steps*(steps+1)/2
    fuel2=0
    for item in x:
        steps=abs(int(item)-math.ceil(statistics.mean(sub)))
        fuel2+=steps*(steps+1)/2
    return fuel1, fuel2

answer1,answer2=bleh(data)

print(answer1,answer2)




