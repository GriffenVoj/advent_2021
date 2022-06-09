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

#only need to calc gamma, epsilon is opposite at every interval

def part1():
    np_data=parse()
    col_sums=np_data.sum(axis=0)
    length=np_data.shape
    epsilon=""
    gamma=""
    for item in col_sums:
        if item < int(length[0])//2:
            gamma+="0"
            epsilon+="1"
        else:
            gamma+="1"
            epsilon+="0"
    return bincon(gamma)*bincon(epsilon)


print(part1())
