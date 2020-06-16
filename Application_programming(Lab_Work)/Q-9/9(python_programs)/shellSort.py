import random

def insertionSort(a,n):
    for h in range(1,int(n/9)):
        while h>0:
            for i in range(h+1,n):
                x=a[i];j=i
                while (j>h and a[j-h]>x):
                    a[j]=a[j-h]
                    j-=h
                a[j]=x
        h=(3*h+1)
    for k in range(n):
      print(a[k],end="\t")


x=list(random.randint(1,50) for i in range(100))
n=len(x);
insertionSort(x,n);
