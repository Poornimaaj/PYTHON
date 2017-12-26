bill_id=input("please enter bill id")
customer_id=input("please enter customer id")
bill_amount=input("please enter the bill amount")
customer_name=input("please enter the customer name")
if((len(customer_name)>=3) and (len(customer_name)<=20)) is True:
    print("bill id:",bill_id)
    print("customer id:",customer_id)
    print("bill amount:Rs. ",bill_amount)
    print("customer name",customer_name)
else:
    print("invalid customer name.customer must be between 3 and 20 characters");
    
