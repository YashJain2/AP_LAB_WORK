my_list=[5,2,9,1]
print("Length :", len(my_list))
print("1st Index :",my_list[0])
my_list2=my_list[0:3]
print("1sr 3 Values :", my_list2)
print("9 in List :", end=" ")
print(9 in my_list)
print("Index for 2 :",my_list.index(2))
print("How Many 2s :",my_list.count(2))
del my_list[(my_list.index(1))]
del my_list[0]
my_list.insert(0,10)
print("Sorted :", my_list.sort())
print("Sorted :", my_list.reverse())
