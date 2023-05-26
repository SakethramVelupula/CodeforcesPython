import math
n,k,l,c,d,p,nl,np=map(int,input().split())
a=math.floor(k*l/nl)
b=c*d
g=math.floor(p/np)
q=min(a,b,g)
print(math.floor(q/n))
