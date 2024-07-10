name = input("Plz enter your name : ")
print("Hello ",name)

message = """
How may i help you sir .

Please select any of them option,
Type 1 >>>> CHECK BALANCE.
Type 2 >>>> DEPOSIT.
Type 3 >>>> WITHDRAWL.
"""
print(message)
task = int(input("plz enter your option : "))
available_amount = 5000 
if task >=1 and task <=3:
    print('Welcome to you in virtual bank program')

    if task == 1:
        # check balance program
        print('Your available amount is : ',available_amount,' INR') 

    elif task == 2 :
        # deposit amount 
        deposit_amount = int(input("Plz enter Deposit Amount : "))
        if deposit_amount >0:
            # available_amount = available_amount + deposit_amount
            available_amount +=  deposit_amount
            print("You have successully Deposited your amount : ",deposit_amount)
            print('Your available amount is : ',available_amount,' INR') 
        else:
            print("plz enter valid amount!")

    else:
        # withdrawl amount
        withdrawl_amount = int(input("plz enter withdrawl amount : "))
        if withdrawl_amount <= available_amount:
             available_amount -= withdrawl_amount
             print('You have succussfully withdrawl your amount : ',withdrawl_amount)
             print('Your available amount is : ',available_amount,' INR') 

        else:
            print("you dont have sufficient amount in your account!")
            print('Your available amount is : ',available_amount,' INR') 

else:
    print("plz choose valid option in between 1 to 3 !")



# same program 
# 3 times 
