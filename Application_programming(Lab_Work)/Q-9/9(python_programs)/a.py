#for loop in python
#val=0
  #for val in range(5):
      #print('val')


#if else condition example

num=3
if num >=0:
    print ('Positive')
else:
    print ('Negative')


#string operation in oython
string="hello"
print (string)
string1=" Python"
print (string + string1)


#boolean values in python

a= True
b= False
print(a)
print(b)
a= not True #means false
b= not False    #means true
print(a)
print(b)


#In operator

animal="dog"
if animal in["lion","cat","dog"]: # if executed as dog is present in in operator
    print('Your animal is in the list')
if animal not in["lion","cat","dog"]:   #if condition won't work as not in states that list if present to not be executed
    print('Animal searched is not present')


#taking user input
name=input("Enter your name ")
age=input("Enter your age   ")
print('Your name is : ' + name)
print('Your age is : ' + age)


#Calculate age
name=input('Enter your name ')
print("What is your age?",(name),"?")
age=int(input('Age : '))
#int means asigning integer type to age variable
days=age*365
print(name,' has been alive for ', days,' days')

#Upper and Loercase functions
name1 = input('Enter your name ')
print(name1.lower())
print(name1.upper())

#NEWLINE IN STRINGS
#\n is fpr newline \t is for tab
print("Natural numbers are :\n1\n2\n3\n4\n5 etc.")


#Combining STRINGS
first_name="Yash "
last_name="Jain"
full_name=first_name + last_name
print(full_name)

#str() functions
name="Yash Jain   "
age=19
total=(name+str(age))  #Converts an integer to a string
print(total)



#Using I/p functions
name=input("What's your name ?\n")
print("Hi "+name+" How are you?")
user=input()
print("Thanks "+name+" GoobBye!!")
