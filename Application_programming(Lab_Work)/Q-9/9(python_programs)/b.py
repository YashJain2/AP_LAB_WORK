#title() functions
#MAkes the first letter capital
name="yash "
name1="jain"
print(name.title() + name1.title())

#Lists in Python

animals=["lion","tiger","dog","cat","birds"]
print(animals)
print(animals[0].title())   #access the first element
print(animals[-1].title())  #access the element from the last i.e. prints bird


#Combinig string and a Lists

message="I love "
print(message + animals[-1].title())
print("I Love " + animals[1].title())

# Changing an element from Lists
animals[2]="birds"
print(animals[-1].title())

#Deleting element from a list

del animals[2]
print(animals)

# Sort and Reverse functions

animals.sort()
print(animals)
animals.sort(reverse=True)
print(animals)
animals.reverse()
print(animals)

#Length element
print(len(animals))

#Using for loop in Lists

for animals in animals:
    print("I love " + animals)
#here nesting is decided by indent


#Using range in loop

for value in range(1,5):
    print(value)


#Using min max sum with numbers Lists

num=[1,2,3,4,5,6]
print("The Sum of List is : ")
print(sum(num))
print("The Maximum Number is : ")
print(max(num))
print("The Minimum Number is : " )
print(min(num))

# Slicing a Lists

print(num[0:2])
print(num[:2])
print(num[3:5])
print(num[3:])


#Using for loop with Slicing

for num in num[1:4]:
    print(num)


#Copying list using slicing List

progLang=["C","java","C++","Python","JavaScript"]
cpy_progLang=progLang[:]
print(progLang)
print("Copied Slicing list is ")
print(cpy_progLang)
cpy_progLang.append('Haskell')
print(cpy_progLang)

#Using Flag to stop looping

i=""
name="Write any name.\n"
while(i!='q'):
    i=input(name)
#Here i is the flag variable and q is the flag word that breaks while loops
