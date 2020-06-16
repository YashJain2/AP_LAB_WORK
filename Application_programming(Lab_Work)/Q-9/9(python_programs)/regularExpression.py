import re

if re.search("ape","The ape is the apex"):
    print("Ape is present")

all_apes=re.findall("ape ","The ape is the apex")
for i in all_apes:
    print(i)
the_str="The ape is the apex"
for i in re.finditer("ape.", the_str):
     loc_tuple=i.span()
     print(loc_tuple)
     print(the_str[loc_tuple[0]:loc_tuple[1]])

animal_str="Cat rat mat fat pat zoo"
all_animals=re.findall("[crmfp]at",animal_str)
some_animals=re.findall("[c-mC-M]at",animal_str)
more_animals=re.findall("[^Cr]at",animal_str)
for i in more_animals:
    print(i)
for i in some_animals:
    print(i)
for i in all_animals:
    print(i)

owl_food="rat cat mat pat"
regex=re.compile("[cr]at")
owl_food=regex.sub("owl",owl_food)
print(owl_food)

rnd_str="Find the \\stuff"
print("Find \\stuff :",re.search("\\stuff",rnd_str))
print("Find \\stuff :",re.search("\\\\stuff",rnd_str))
print("Find \\stuff :",re.search(r"\\stuff",rnd_str))

rand_str="C.B.I. F.B.I.  I.A.S. CIA"
print("Matches :",len(re.findall("\..\..\..",rand_str)))

rand_str="""This is a text paragraph
that goes on for
multiple lines"""
print(rand_str)
regex=re.compile("\n")
rand_str=regex.sub(" ",rand_str)
print(rand_str)


rand_str="12345"
print("Matches :",len(re.findall("\d",rand_str)))
print("Matches :",len(re.findall("/D",rand_str)))

if re.search("\d{5}",rand_str):
    print("It a a zip code")

if re.search("\w{2,20}\s\w{2,20}", "Yash Jain"):
    print("It is a valid name")

if re.search("[\w]{2,10}@\w{5}.\w{3}","yjain8958372013@gmail.com"):
    print("Valid E-mail")

rand_str="doctor doctors doctor's"
regex=re.compile("[doctor]+s")
matches=re.findall(regex,rand_str)
print("Matches :", len(matches))
regex=re.compile("[doctor]+['s]{0,2}")
matches=re.findall(regex,rand_str)
print("Matches :", len(matches))
