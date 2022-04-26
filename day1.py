data=open("day1data.txt").readlines()

newdata=[]
for item in data:
    sub=""
    sub+=item
    newdata.append(int(sub))

slide=[]


a=1
b=2
c=3
counter=0

for i in newdata:
    try:
        num=newdata[a]+newdata[b]+newdata[c]
        num2=newdata[a+1]+newdata[b+1]+newdata[c+1]
    except:
        if c>len(newdata):
            counter+=0
        
    if num2>num:
        counter+=1
    a+=1
    b+=1
    c+=1
print(counter)
        
