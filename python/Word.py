s=str(input())
u=0
l=0
for x in s:
    if(x==x.upper()):
        u=u+1
    else:
        l=l+1
if(u>l):
    print(s.upper())
else:
    print(s.lower())
