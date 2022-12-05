
with open("Advent_code_2022/Q4/Adven_4.txt") as f:
    c = 0
    l = f.readlines()
    # print(l)
    for i in l:
        q = i.split(",")
        a = q[-1]
        q.pop(-1)
        q.append(a[0:len(a)-1])
        # print(q)
        start = q[0].split("-")
        end = q[1].split("-")
        d = []
        b = []
        for m in range(int(start[0]), int(start[1])+1):
            d.append(m)
        for k in range(int(end[0]), int(end[1])+1):
            b.append(k)
        p = [value for value in d if value in b] #set(b)&set(d)
        # print(p)
        if (len(p) > 0):
            c = c+1

    print(c)
