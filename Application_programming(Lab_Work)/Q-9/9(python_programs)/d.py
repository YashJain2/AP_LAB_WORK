#Defining Functions in Python

def function():
    print("Hello we are in our function")

print("We are in our main program")
function()

#Arguments and parameters in functions

def names(full_name,last_name):
    print("Your first name is " + full_name)
    print("Your last name is " + last_name)
names('Yash','Jain')

#Default values in functions

def sum(num1=1,num2=5): #default values are 1nd 5
    x=num1+num2
    print(x)
sum()
sum(10,9)

#return values in Functions

def addition(a,b):
    total=a+b
    return total
print("Addition is : ", addition(2,7))


#Classes in Python
class Person():#Creating a class of person
    def insert(self,name,age,idNumber):
        self.name=name
        self.age=age
        self.idNumber=idNumber
    def output(self):
        print("Your name is " +self.name +" your age is " +self.age+ " and your idNumber is "+self.idNumber)
j=Person()#Creates j as an class object
j.insert('Yash','20','7323693')
j.output()
print(j.name)

#Constructor__init__(self) functions

class Person():#Creating a class of person
    def __init__(self,name,age,idNumber):
        self.name=name
        self.age=age
        self.idNumber=idNumber
    def output(self):
        print("Your name is " +self.name +" your age is " +self.age+ " and your idNumber is "+self.idNumber)
j=Person('Yash','20','7323693')
j.output()
#Accessing variables and functions of an objects
print(j.name)
print(j.age)
print(j.idNumber)


#Creating multiple instances/objects in class
m=Person('Preeti','35','001232')
m.output()
print("The Employeee age is  "+m.age)

#Class inheritance
class Msg():
    def message(self):
        print('Child is sweet')
class Child(Person,Msg):
    pass #i.e.it inherits all features of Person class
kid=Child('Prasukh','5','null')
kid.output()
kid.message()
