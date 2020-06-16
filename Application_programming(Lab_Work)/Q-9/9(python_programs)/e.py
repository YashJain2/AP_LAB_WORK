samp_string="  This is a very important string"
samp_string=samp_string.lstrip()
print("Uppercase :",samp_string.upper())
print("Lowercase :",samp_string.lower())
list_of_words=samp_string.split()
print("Words")
for words in list_of_words:
    print(words)
print("How many ts? ", samp_string.count('t'))
print("String Index :",samp_string.find("string"))
print("Replace very :",samp_string.replace("very","kind of"))
letter="z"
print("Is \"z\" a letter or number :",letter.isalnum())

print("Is \"z\" a letter :",letter.isalpha())

print("Is \"z\" a number :",letter.isdigit())

print("Is \"z\" a space :",letter.isspace())


#random number in a list
import random
num_list=[]
for i in range(5):
    num_list.append(random.randrange(1,9))
for i in num_list:
    print(i)
