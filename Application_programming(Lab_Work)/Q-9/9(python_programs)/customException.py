try:
    a_list=[1,2,3]
    print(a_list[3])
except IndexError:
    print("Sorry, index doesn't exist")
except:
    print("An unknown error occurred")


try:
    my_file=open("my_data.txt",encoding="utf-8") 

except FileNotFoundError as ex:
    print("{} doesn't exist".format(my_file))
    print(ex.args)
else:
    print("File is open :",my_file.read())
    my_file.close()
finally:
    print("Finished working")
