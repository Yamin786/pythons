import json 
file_name = "user_data.json"
try:
    with open(file_name,"r") as file:
        data = json.load(file)
except:
    data  = []
print("What you want ot do ?")
print("1.Make Account \n2.Delete Account \n3.Add Money \n4.Share to Other \n5.Balance Inquiry")
choice = int(input("Enter a Choice(1-5) :"))
def create_account(data):
    user_name = input("Enter a username :")
    password = input("Enter a password :")
    accn  = input("Enter an unique account number :")
    print("Don't share account number and password to anyone.")
    first_balance = int(input("Enter the amount :"))
    balance = first_balance
    accn_exists = any(user["accn"] == accn for user in data)
    if accn_exists:
        print("This account has already taken.")
    else:   
        new_user = {
            "username":user_name,
            "password":password,
            "balance":balance,
            "accn":accn
        }       
        data.append(new_user)
        with open(file_name,"w") as file:
            json.dump(data,file,indent=4)   
def  delete_account(data):
    accn = input("Enter account number :")
    password = input("Enter password :")
    pass_exists = any(user["password"]== password for user in data)
    accn_exists = any(user["accn"] == accn for user in data)
    if accn_exists and pass_exists:
        print(f"Request has been recived for delete {accn} account")
    else:
        print("There is no account like this")
def add_money(data):
    accn = input("Enter account number :")
    password = input("Enter password :")
    user_index = next((i for i,user in enumerate(data) if user["accn"]==accn and user["password"]==password),-1)
    if user_index == -1:
        print("There is no such account. If you have account try the correct ones.")
    else:
        user_balance = data[user_index]["balance"]
        add_amount = int(input("Enter the amount you want to add :"))
        user_balance+=add_amount
        data[user_index]["balance"] = user_balance
        with open(file_name,"w") as file:
            json.dump(data,file,indent=4)
        print(f"Add money {add_amount} is successfull.")
def share_to_other(data):
    accn = input("Enter your account number :")
    password = input("Enter password :")
    user_index = next((i for i,user in enumerate(data) if user["accn"]==accn and user["password"]==password),-1)
    if user_index == -1:
        print("There is no such account. If you have account try the correct ones.")
    else:
        accn_to_share = input("Enter the account number where you want to share money :")
        share_user_index = next((i for i,user in enumerate(data) if user["accn"]==accn_to_share),-1)
        if share_user_index == -1:
            print("There is no such account to share.")
        else:
            balance_to_move = int(input("Enter the amount to share :"))
            data[user_index]["balance"] -= balance_to_move
            data[share_user_index]["balance"] += balance_to_move
            with open(file_name,"w") as file:
                json.dump(data,file,indent=4)
        print(f"{balance_to_move} shared to account {accn_to_share}.")
def balance_inquiry(data):
    accn = input("Enter your account number :")
    password = input("Enter password :")
    user_index = next((i for i,user in enumerate(data) if user["accn"]==accn and user["password"]==password),-1)
    if user_index == -1:
        print("There is no such account. If you have account try the correct ones.")
    else:
        balance_details = data[user_index]["balance"]
        name = data[user_index]["username"]
        account = data[user_index]["accn"]
        print(f"Dear {name} your account number is '{account}' and the balance amount is '{balance_details}'")
if choice == 1:
    create_account(data)
elif choice == 2:
    delete_account(data)
elif choice == 3:
    add_money(data)
elif choice == 4:
    share_to_other(data)
elif choice == 5:
    balance_inquiry(data)
else:
    print("You entered a wrong option. Please try among the options given(1-5)")
