n=int(input())
s=str(input())
count=0
for i in range(0,len(s)-1):
    if(s[i]==s[i+1]):
        count=count+1
print(count)
