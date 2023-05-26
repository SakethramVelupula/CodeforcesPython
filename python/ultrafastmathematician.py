s1=str(input())
s2=str(input())
s3=[]
for i in range(0,len(s1)):
    if(s1[i]==s2[i]):
        s3.append("0")
    else:
        s3.append("1")
for i in s3:
    print(i,end="")
