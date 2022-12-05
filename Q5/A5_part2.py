with open("Advent_code_2022/Q5/Adven_5.txt") as f:
    l=f.readlines()
    print(l)
    l0=[]
    l1=["F","D","B","Z","T","J","R","N"]
    l2=["R","S","N","J","H"]
    l3=["C","R","N","J","G","Z","F","Q"]
    l4=["F","V","N","G","R","T","Q"]
    l5=["L","T","Q","F"]
    l6=["Q","C","W","Z","B","R","G","N"]
    l7=["F","C","L","S","N","H","M"]
    l8=["D","N","Q","M","T","J"]
    l9=["P","G","S"]
    
    all=[l0,l1,l2,l3,l4,l5,l6,l7,l8,l9]
    # l1=["Z","N"]
    # l2=["M","C","D"]
    # l3=["P"]
    # all=[l0,l1,l2,l3]
    print(all)
    for i in l:
        t=i.split(" ")
        temp=t[-1]
        t.pop()
        t.append(temp[0:len(temp)-1])
        q=[]
        for p in t:
            if(p.isdigit()):
                q.append(int(p))

        print(q)
        temp_stack=[]
        for k in range(0,q[0]):
            temp_ind=all[q[1]].pop()
            temp_stack.append(temp_ind)
        for j in range(0,len(temp_stack)):
            all[q[2]].append(temp_stack[len(temp_stack)-j-1])

            

    print(all)
    for i in range(1,len(all)):
        print(all[i][-1],end="")

