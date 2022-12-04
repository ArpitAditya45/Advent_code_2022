from collections import Counter
dic={}#creating a dictionary for mapping
a="a"
for i in range(1,27):
    dic[a]=i
    a=chr(ord(a)+1)

a="A"
for i in range(27,53):
    dic[a]=i
    a=chr(ord(a)+1) 
# print(dic)
sum=0
with open("Adven_3.txt") as f:
    line=f.readlines()
    # print(line)
    for i in range(0,len(line)-2,3):
        a=line[i]
        a=a[0:len(line[i])-1]
        b=line[i+1]
        b=b[0:len(line[i+1])-1]
        
        c=line[i+2]
        c=c[0:len(line[i+2])-1]
        print(c)
        dict1=(Counter(a))
        dict2=(Counter(b))
        dict3=(Counter(c))

        common=dict1 & dict2 & dict3 #finding common element
        common=list(common.elements())
        sum=sum+dic.get(common[0])
    print(sum)
        

