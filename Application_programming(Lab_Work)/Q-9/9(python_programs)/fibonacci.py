def fibonacci (num):
    if  num==0:
        return 0
    elif num==1:
        return 1
    else:
        result=fibonacci(num-1)+fibonacci(num-2)
        return result

print("5th Term in fibonacci series is :",fibonacci(5))
#function prints fibonacci numbers at the given position num
num_value=int(input("Enter the number of terms user wants in fibonacci series :"))
i=0
while i<num_value:
    fib_value=fibonacci(i)
    print(fib_value, end=" ")
    i+=1
