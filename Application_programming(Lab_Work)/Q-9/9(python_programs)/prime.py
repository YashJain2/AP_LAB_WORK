def is_prime(num):
    for i in range(2,num):
        if(num%i)==0:
            return False
    return True

def get_prime(max_number):
    list_of_primes=[]
    for num1 in range(2,max_number):
        if is_prime(num1):
            list_of_primes.append(num1)
    return list_of_primes

max_num=int(input("Search for prime upto : "))
list_of_primes=get_prime(max_num)
for prime in list_of_primes:
    print(prime)