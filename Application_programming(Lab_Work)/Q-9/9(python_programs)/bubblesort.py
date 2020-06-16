import random
num_list=[]
for i in range(5):
    num_list.append(random.randrange(1,9))
print(num_list)
for x in range(5):
    for y in range(5-x):
        if y+1<5:
            if num_list[y] > num_list[y+1]:
                #print("Switch",num_list)
                temp=num_list[y]
                num_list[y]=num_list[y+1]
                num_list[y+1]=temp
print(num_list)
