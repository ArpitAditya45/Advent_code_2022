with open("Advent_code_2022/Q6/Adven_6.txt") as f:
    a = f.read()
    b = a
    n = 14
    p = 0
    w = ""
    dict_1 = {}
    r = 0
    while (p < len(a)):

        if (p < n):
            w = w+a[p]

            if (dict_1.get(a[p]) == None):
                dict_1[a[p]] = 1

            else:
                dict_1[a[p]] = dict_1.get(a[p])+1
            p = p+1
            
        else:
            
            val = True
            for i in dict_1:
                if (dict_1.get(i) >= 2):
                    val = False
                    break

            if (val):
                print(p)
                # print(dict_1)
                break
            dict_1[a[r]] = dict_1.get(a[r])-1

            if (dict_1.get(a[p]) == None):
                dict_1[a[p]] = 1
            else:
                dict_1[a[p]] = dict_1.get(a[p])+1
            r = r+1
            p = p+1

            w = a[r:p]
            
