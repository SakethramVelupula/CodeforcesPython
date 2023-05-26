s=str(input())
if(s[0]==s[0].upper()):
    print(s)
else:
    print(s[0].upper(),end="")
    print(s[1:len(s)])
