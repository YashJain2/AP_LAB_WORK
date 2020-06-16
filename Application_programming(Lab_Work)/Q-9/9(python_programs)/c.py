#If/else statements

var=10
if var==10:
    print("Number is 10")
else:
    print("The number is not 10")


#Using Tuples

tuple = (200,100,20)
print(tuple[0])
print(tuple[-1])
for tuple in tuple:
    print(tuple)
#Overwriting a Tuples
tuple=(200,100,10)

#Compare STRINGS
name1="Yash"
name2="jain"
if name1==name2:
    print("Strings are equal")
else:
    print("Strings are not equal")

#Not equal with if else statements
if name1!=name2:
    print("Both are not equal")


#Using AND OR operatorwith if else statements
num1=10
num2=5
if (num1>=num2 and num1>=0):
    print("The Result of AND operator is True")
if(num1<0 or num2>num1):
    print("The Result of OR operator is True")
else:
    print("Result of OR operator is False")


# if else statements with lists
names=['Yash','Riya','Gauri','Preeti']

if ('Yash' and 'Preeti' in names):
    print("Name is in the list")
else:
    print("Name is not present")


#if-elif else statements

grade=85
if grade>90:
    print("Your grade ",grade," is A+")
elif grade>80 and grade<=90:
    print("Your grade ",grade," is A")
else:
    print("Your grade ",grade," is not satisfactory")


#Dictionaries in Python

dic={'Animals':'Birds','Cars':'BMW','Subjects':'Maths'}
print(dic['Animals'])
print(dic['Cars'])


#Adding new key/value to dictionary

dic['Color']='White'
print(dic['Color'])

#deleting a key from dictionary
print(dic)
del dic['Color']
print("After deleting Color :\n",dic)

#While loops
#using break and continuestaements with while loop

i=1
while(i<=10):
    print(i)
    if i==5:
        break
    elif i==2:
        i+=2
        continue
    i+=1    #Loops until condition becomes false at i=11
