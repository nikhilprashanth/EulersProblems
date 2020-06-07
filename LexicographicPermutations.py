l=[0,1,2,3,4,5,6,7,8,9]

def perm(l,count,lim):
    #print("l = ", l, "count= ", count, "lim= ",lim)

    if len(l)==2:
        l1=[]
        l1.append(l[0])
        l1.append(l[1])
        l3 = []
        l3.append(l1)
        count = count + 1
        if count >= lim:
            return l3, count
        
        l2=[]
        l2.append(l[1])
        l2.append(l[0])
        l3.append(l2)
        count = count + 1
        return l3, count

    all_comb = []
    i = 0
    while i<len(l):
        e=l[i]
        l.pop(i)
        w, count=perm(l,count,lim)
        
        for elem in w:
            new_elem = [e]
            new_elem += elem
            all_comb.append(new_elem)

        l.insert(i, e)
        if count >= lim:
            return all_comb, count
        i = i + 1

    return all_comb, count

def list_to_num(item):
    mult = 1
    num = 0
    for i in range(len(item)-1, -1, -1):
        num += item[i] * mult
        mult *= 10

    return num

lim=1000
w, count=perm(l,0,lim)
#print("complete list = ", w)
print(" ", lim, " item (list format) is ", w[lim-1])
print(" item (number format) is ", list_to_num(w[lim-1]))
print("The length of the complete list is ",len(w))

    
