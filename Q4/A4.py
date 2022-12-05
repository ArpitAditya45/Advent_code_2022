
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
        if ((int(start[0]) <= int(end[0]) and int(start[1]) >= int(end[1])) or (int(start[0]) >= int(end[0]) and int(start[1]) <= int(end[1]))):

            c = c+1

    print(c)
