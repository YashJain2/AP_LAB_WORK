#Sum of an unknown args
def sum_all(*args):
    sum1=0
    for i in args:
        sum1+=i
    return sum1
print("Sum : ", sum_all(2,43,39,20))
