from collections import Counter
dic={}
a="a"
for i in range(1,27):
    dic[a]=i
    a=chr(ord(a)+1)

a="A"
for i in range(27,53):
    dic[a]=i
    a=chr(ord(a)+1)
print(dic)
sum=0
with open("Adven_3.txt") as f:
    line=f.readlines()
    # print(line)
    for i in line:
        a=i[0:len(i)-1]
        l=[a[0:len(i)//2],a[len(i)//2:]]
        dict1=(Counter(l[0]))
        dict2=(Counter(l[1]))
        common=dict1 & dict2
        common=list(common.elements())
        sum=sum+dic.get(common[0])
    print(sum)
        

