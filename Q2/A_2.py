with open("Adven_2.txt") as f:
    line=f.readlines()
    scores={"X":1,"Y":2,"Z":3}
    sum=0
    print(line)
    for i in line:
        l=i.split(" ")
        a=l[-1][0:1]
        l.pop(len(l)-1)
        l.append(a)
        temp=scores.get((l[-1]))
        sum=sum+temp
        if(l[0]=='A'):
            if(l[-1]=="X"):
                sum=sum+3
            else:
                if(l[-1]=="Y"):
                    sum=sum+6
        elif(l[0]=="B"):
            if(l[-1]=="Y"):
                sum=sum+3
            else:
                if(l[-1]=="Z"):
                    sum=sum+6
        else:
            if(l[-1]=="Z"):
                sum=sum+3
            else:
                if(l[-1]=="X"):
                    sum=sum+6
            
    print(sum)
            
        
