l=['A','E','I','O','U','a','e','i','o','u','Y','y']
s=str(input())
a=s.lower()
for x in a:
    if(x not in l):
        print(".",end="")
        print(x,end="")
