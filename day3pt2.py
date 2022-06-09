#go through each column and determine most common number 
#ties go to 1
#remove columns that DONT start with that number
#repeat until one column remains
import numpy as np


def parse():
    data=open("data.txt").read().splitlines()
    oneline=[]
    everyline=[]
    for item in data:
        for num in item:
            oneline.append(int(num))
        everyline.append(oneline)
        oneline=[]
    parsed_data=np.array(everyline)
    return parsed_data

#need to input str
def bincon(binum):
    n=len(binum)-1
    num=0
    for i in range(len(binum)-1,-1,-1,):
        if binum[i]=="1":
            num+=2**(n-i)
    return num

#gamma, ep
def mostcommon(data_set,i,gamma):
    col_sums=list(data_set.sum(axis=0))
    length=data_set.shape
    if  int(length[0])/2 > col_sums[i] :
       if gamma:
            return 0
       else: return 1
    elif gamma: return 1
    else: return 0
        

def part2():
    index=0
    data_g=parse()
    data_e=np.array(data_g,copy=True)
    rows_g=data_g.shape[0]
    rows_e=data_e.shape[0]
    to_keep_g=[]
    to_keep_e=[]
    while rows_e>1 or rows_g>1:
        new_e=[]
        new_g=[]
        if rows_g>1:
            g=mostcommon(data_g,index,True)
            for item in range(len(data_g)):
                if data_g[item][index]==g:
                    to_keep_g.append(item)
            for x in to_keep_g:
                new_g.append(data_g[x])
            to_keep_g=[]
            data_g=np.array(new_g)
            new_g=[]
            rows_g=data_g.shape[0]
        if rows_e>1:
            e=mostcommon(data_e,index,False)
            for item in range(len(data_e)):
                if data_e[item][index]==e:
                    to_keep_e.append(item)
            for x in to_keep_e:
                new_e.append(data_e[x])
            to_keep_e=[]
            data_e=np.array(new_e)
            new_e=[]
            rows_e=data_e.shape[0]
        index+=1
        gamma=""
        epsilon=""
        for i in range(len(data_g[0])):
            gamma+=str(data_g[0][i])
            epsilon+=str(data_e[0][i])
    return bincon(gamma)*bincon(epsilon)

print(part2())
        

        

    
