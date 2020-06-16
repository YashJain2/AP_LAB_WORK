i=int(input(""));
t=0
x=0
while t<i and (i>=1) and (i<=100):
    n,k=input("").split();
    n=int(n); k=int(k)
    if  (n <=1000000) and (n>=2) and (k>=1)and (k<=1000000000):
        b=n
        for j in range(2,b+1):
            if n%j==0:
                n+=j
                break
        print(n + 2*(k-1))
    t+=1

    
for i in range(int(input())):
	n,k=map(int,input().split(" "))
	for i in range(2,n+1):
			if n%i==0:
				break
	print(n+i+(k-1)*2)
