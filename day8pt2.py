
def part1(x):
    sub=[]
    for item in x:
        sub2=item.split("|")
        sub.append(sub2[1])
    counter=0
    for ele in sub: 
        sub3=ele.split(" ")
        print(sub3)
        for z in sub3:
            if int(len(z))==3 or int(len(z))==4 or int(len(z))==2 or int(len(z))==7:
                counter+=1
                print(counter)

    return counter

data=open("data.txt").read().splitlines()


def part2(x):
    counter=0
    for item in x:
        y,z=item.split("|")
        length={len(a):set(a) for a in y.split()}
        n=""
        z=z.split(" ")
        y=y.split(" ")
        for ele in z:
            if len(ele)==2:
                n+="1"
            elif len(ele)==3:
                n+="7"
            elif len(ele)==4:
                n+="4"
            elif len(ele)==7:
                n+="8"

            elif len(ele)==5:
                #5 check
                if len(set(length[2])&set(ele))==2:
                    
                    n+="3"
                elif len(set(length[4])&set(ele))==3:
                    n+="5"
                    #3 check 

                else:
                    
                    n+="2"
                    print(n)
            elif len(ele)==6:
                #6
                if len(set(length[3])&set(ele))==2:
                    
                    n+="6"
                elif len(set(length[4])&set(ele))==4:
                    n+="9"
                    
                else:
                    n+="0"
        counter+=int(n)
    return counter

print(part2(data))









