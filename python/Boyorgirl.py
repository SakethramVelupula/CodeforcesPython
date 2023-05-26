s=str(input())
l=[]
for i in s:
    l.append(i)
x=len(set(l))
if(x%2==0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
