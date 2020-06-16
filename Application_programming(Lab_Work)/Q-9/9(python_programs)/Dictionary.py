customers=[]
while True:
    create_entry=input("Enter Customer (Yes/No) : ")
    create_entry=create_entry.lower()
    if create_entry =="no":
        break
    else:
        f_name,l_name=input("Enter Customer Name : ").split()
        customers.append({"f_name":f_name,"l_name":l_name})
        #created a dictionary of customers
for cust in customers:
    print(cust['f_name'],cust['l_name'])
    #accessing the valuses of fname and l_name from the dictionary using key

derek_dict={"f_name":"Derek","l_name":"Banas","address":"123 Main St"}
print("First Name :",derek_dict['f_name'])
derek_dict["address"]="215 North St"
print("New Address :", derek_dict['address'])
derek_dict['city']="Pittsburgh"
print("Is there a city :","city" in derek_dict)
del derek_dict['f_name']
for k,v in derek_dict.items():
    print(k,v)
    
