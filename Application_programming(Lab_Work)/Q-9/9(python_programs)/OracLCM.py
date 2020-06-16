from math import *
a=int(input())
b=list(map(int,input().split()))
l=(b[0]*b[1])//gcd(b[0],b[1])
g=gcd(b[0],b[1])
for i in b[2:]:
    l=gcd(l,(i*g)//gcd(i,g))
    g=gcd(i,g)
print(l)
