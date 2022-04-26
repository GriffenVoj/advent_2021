data=open("data.txt").read().split("\n")
import numpy as np
def parse(x):
    sub1=[]
    for item in x:
        sub1.append(item.split(" -> "))    
    return sub1

new=parse(data)

def split(z):
    first=z[0].split(",")
    second=z[1].split(",")
    a=int(first[0])
    b=int(first[1])
    c=int(second[0])
    d=int(second[1])
    return a,b,c,d


def answerer(b):
    diagram=np.zeros((1000,1000), dtype=int)
    for item in b:
        x1,y1,x2,y2=split(item)
        if x1==x2:
            diagram[y1][x1]+=1
            diagram[y2][x2]+=1
            y=y1-y2
            if y>1:
                for i in range(1,abs(y)):
                    diagram[y1-i][x1]+=1
            elif y<1:
                for i in range(1,abs(y)):
                    diagram[y2-i][x1]+=1
        if y1==y2:
            diagram[y1][x1]+=1
            diagram[y2][x2]+=1
            x=x1-x2
            if x>1:
                for i in range(1,abs(x)):
                    diagram[y1][x1-i]+=1
            elif x<1:
                for i in range(1,abs(x)):
                    diagram[y1][x2-i]+=1
        if x1>x2 and y1>y2:
            diagram[y1][x1]+=1
            diagram[y2][x2]+=1
            x = x1-x2
            y = y1-y2
            if abs(x)>abs(y):
                for i in range(1,abs(x)):
                    diagram[y1-i][x1-i]+=1
            else:
                for i in range(1,abs(y)):
                    diagram[y1-i][x1-i]+=1
        if x1<x2 and y1<y2:
            diagram[y1][x1]+=1
            diagram[y2][x2]+=1
            x = x1-x2
            y = y2-y1
            if abs(x)>abs(y):
                for i in range(1,abs(x)):
                    diagram[y1+i][x1+i]+=1
            else:
                for i in range(1,abs(y)):
                    diagram[y1+i][x1+i]+=1
        if x1>x2 and y1<y2:
            diagram[y1][x1]+=1
            diagram[y2][x2]+=1
            x = x1-x2
            y = y1-y2
            if abs(x)>abs(y):
                for i in range(1,abs(x)):
                    diagram[y1+i][x1-i]+=1
            else:
                for i in range(1,abs(y)):
                    diagram[y1+i][x1-i]+=1
        if x1<x2 and y1>y2:
            diagram[y1][x1]+=1
            diagram[y2][x2]+=1
            x = x1-x2
            y = y2-y1
            if abs(x)>abs(y):
                for i in range(1,abs(x)):
                    diagram[y1-i][x1+i]+=1
            else :
                for i in range(1,abs(y)):
                    diagram[y1-i][x1+i]+=1
    return len(np.where(diagram>=2)[0])

print(answerer(new))






