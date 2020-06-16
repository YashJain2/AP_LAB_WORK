import random

print([2*x for x in range(1,11)])

print([x for x in range(0,11) if x%2==0])

print([x*y for x in range(1,3) for y in range (11,16)])

print([x for x in[random.randint(1,1001) for i in range(50)] if x % 1==0])


mult_list=[[1,2,3],[4,5,6],[7,8,9]]

print([col[1] for col in mult_list])

print([mult_list[i][i] for i in range(len(mult_list))])
