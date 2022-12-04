with open("Adven_2.txt") as f:
    line=f.readlines()
    scores={"A":1,"B":2,"C":3}
    sum=0
    print(line)
    for i in line:
        l=i.split(" ")
        a=l[-1][0:1]
        l.pop(len(l)-1)
        l.append(a)
        if(l[-1]=="Z"):
            if(l[0]=="A"):
                sum=sum+scores.get("B")
            if(l[0]=="B"):
                sum=sum+scores.get("C")
            if(l[0]=="C"):
                sum=sum+scores.get("A")
            sum=sum+6
        elif(l[-1]=="Y"):
            if(l[0]=="A"):
                sum=sum+scores.get("A")
            if(l[0]=="B"):
                sum=sum+scores.get("B")
            if(l[0]=="C"):
                sum=sum+scores.get("C")
            sum=sum+3

        else:
            if(l[0]=="A"):
                sum=sum+scores.get("C")
            if(l[0]=="B"):
                sum=sum+scores.get("A")
            if(l[0]=="C"):
                sum=sum+scores.get("B")
            
    print(sum)

        
            
        
