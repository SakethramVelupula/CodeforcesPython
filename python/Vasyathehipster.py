a,b=map(int,input().split())
c=min(a,b)
print(c,end=" ")
d=max(a,b)-min(a,b)
if(d%2==0):
    print(int(d/2))
else:
    print(int((d-1)/2))
