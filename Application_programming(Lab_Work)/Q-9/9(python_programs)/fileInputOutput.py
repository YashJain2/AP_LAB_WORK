import os

with open("my_data.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("Some random texts\n Sone more texts \n And again and again")

with open ("my_data.txt", encoding="utf-8") as my_file:
    print(my_file.read())

print(my_file.closed)
print(my_file.name)
print(my_file.mode)

#Reading line one by one
with open("my_data.txt", encoding="utf-8") as my_file:
    line_num =1
    while True:
        line =my_file.readline()
        if not line:
            break
        line1=line.replace(" ","")
        list=[]
        list=line.split()
        print("Line ",line_num)
        print("Number of words :", len(list))
        x=(len(line1)/len(list))
        print("Avg Word Length : {:.1f}".format(x) )
        line_num +=1
