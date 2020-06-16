import math

for _ in range(int(input())):
    a,b=input().split()
    a=int(a);b=int(b)
    c,d=input().split()
    c=int(c);d=int(d)
    result=(a*b)+(c*d)
    result1=math.sqrt(result)
    x=int(result1)
    if x==result1 and ((a!=b) and (c!=d)) and ((x==a) or (x==b)) and ((x==c) or (x==d)) and ((x==a+c) or (x==b+c) or (x==b+d) or (x==a+d)):
        print("yes")
    else:
        print("no")
