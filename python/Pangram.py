n=int(input())
s=str(input())
s=s.lower()
l=list(s)
x=len(set(l))
if x==26:
    print("YES")
else:
    print("NO")
