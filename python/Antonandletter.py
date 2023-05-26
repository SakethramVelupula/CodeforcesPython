s=str(input())
if(len(s)>2):
    l=list(s)
    p=[]
    p.append(l[1])
    for i in range(4,len(l),3):
        p.append(l[i])
    q=set(p)
    print(len(q))
else:
    print("0")
