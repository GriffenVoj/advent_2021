data=open("data.txt").read().splitlines()
oneline=[]
all_line=[]
for item in data:
    oneline=[1 if x==">" else 2 if  x=="v" else 0 if x=="." else x for x in item]
    all_line.append(oneline)
import numpy as np
all_line=np.array(all_line)
dimmensions=np.shape(all_line)
x=dimmensions[1]
y=dimmensions[0]

#disapearring twos
#add new free space after 1s move
def whenstop(matrix,counter,xdim,ydim):
    submatrix=np.array(matrix,copy=True)
    eastwhere=list(zip(*np.where(submatrix==1)))
    southwhere=list(zip(*np.where(submatrix==2)))
    freespace=list(zip(*np.where(submatrix==0)))
    for item in eastwhere: 
        sub=(item[0],item[1]+1)
        if item[1]+1==xdim and (item[0],0) in freespace:
            submatrix[item[0]][item[1]]=0
            submatrix[item[0]][0]=1
            freespace.remove((item[0],0))
        if sub in freespace:
            submatrix[item[0]][item[1]]=0
            submatrix[item[0]][item[1]+1]=1
            freespace.remove(sub)
    freespace=list(zip(*np.where(submatrix==0)))
    for element in southwhere:
        sub=(element[0]+1,element[1])
        if element[0]+1==ydim and (0,element[1]) in freespace:
            submatrix[element[0]][element[1]]=0
            submatrix[0][element[1]]=2
            freespace.remove((0,element[1]))
        if sub in freespace:
            submatrix[element[0]][element[1]]=0
            submatrix[element[0]+1][element[1]]=2
            freespace.remove(sub)
    counter+=1
    print(counter)
    if (matrix==submatrix).all(): 
        return counter
    else:
        matrix=submatrix
        return whenstop(matrix,counter,xdim,ydim)



print(whenstop(all_line,0,x,y))