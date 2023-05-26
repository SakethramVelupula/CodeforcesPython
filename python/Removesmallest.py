t=int(input())
while(t>0):
    c=0
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    for i in range(1,n):
        if l[i]-l[i-1]>1:
            c=c+1
            print("NO")
            break
    if c==0:
        print("YES")
    t=t-1
