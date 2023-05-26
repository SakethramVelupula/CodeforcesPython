s1=str(input())
s2=str(input())
s3=str(input())
s4=s1+s2
l3=list(s3)
l4=list(s4)
l3=sorted(l3)
l4=sorted(l4)
count=0
if(len(l3)==len(l4)):
    for i in range(0,len(l3)):
        if(l3[i]==l4[i]):
            count+=1
    if(count==len(l3)):
        print("YES")
    else:
        print("NO")
else:
    print("NO")

