data=open("s.txt").read().split(",")

def parse(x):
    sub=[]
    for item in x:
        sub.append(int(item))
    dicts={}
    for i in range(9):
        amnt=sub.count(i)
        dicts[i]=amnt
    return dicts

newdata=parse(data)

def answer(z):
    for day in range(80):
        dictd={}
        values=[]
        keys=[]
        special=0
        for key, value in z.item():
            if key == 0:
                keys.append(0)
                value.append(z[0])
                print(keys)
                special+=int(z[0])
            elif key == 7:
                special+=int(z[7])
            else:
                keys.append(key)
                values.append(key[value])
        dictd=dict(zip(keys,values)
        dictd[6]=special
        final=0
    for key, value in z:
        final+=int(key[value])
    return final


print(answer(newdata))
