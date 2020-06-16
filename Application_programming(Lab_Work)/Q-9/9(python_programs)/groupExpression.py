import re

bd=input("Enter yor birth date (dd-mm-yyyy) :")
regex=re.search(r"(\d{1,2})-(\d{1,2})-(\d{1,4})",bd)
print("Your birth date is on :",regex.group())
print("Your birth year is on",regex.group(3))

match=re.search(r"\d{2}","The weighs 30 lbs")
print("Match :",match.group())
print("Match :",match.span())
print("Match :",match.start())
print("Match :",match.end())
