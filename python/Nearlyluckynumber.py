s=str(input())
a=['4','7']
count=0
for i in s:
    if i in a:
        count=count+1
if count==4 or count==7:
    print("YES")
else:
    print("NO")
