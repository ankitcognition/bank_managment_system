# menu function
def menu():
    print('WELCOME TO BANK MANAGEMENT SYSTEM')
    print('='*35)
    print('1)CREATE ACCOUNT')
    print('2)DEPOSIT MONEY')
    print('3)WITHDRAW MONEY')
    print('4)CHECK BALANCE')
    print('5)TRANSFER MONEY')
    print('6)SEARCH ACCOUNT')
    print('7)DELETE ACCOUNT')
    print('8)VIEW ALL ACCOUNTS')
    print('9)EXIT')
    print('='*35)

#function to repeat menu 
def choice():
    while True:
        menu()
        try:
            user_input=int(input("PLEASE SELECT YOUR ACTION FROM THE MENU(1-9): "))
            if user_input==1:
                #create account function
                print("Feature coming soon...")
            elif user_input==2:
                #deposit money function
                print("Feature coming soon...")
            elif user_input==3:
                #withdraw money function
                print("Feature coming soon...")
            elif user_input==4:
                #check balance function
                print("Feature coming soon...")
            elif user_input==5:
                #transfer money funtion
                print("Feature coming soon...")
            elif user_input==6:
                #search account function
                print("Feature coming soon...")
            elif user_input==7:
                #delete account function
                print("Feature coming soon...")
            elif user_input==8:
                #view all accounts function
                print("Feature coming soon...")
            elif user_input==9:
                #exit function
                print("Feature coming soon...")
                break
            else:
                print("SELECT VALID ACTION")
                
        except ValueError:
            print("ENTER VALID NUMBER(1-9)")
            continue
choice()

# create account function
accounts=[]
def create_acc():
    while True:
      try:
        acc_no=int(input('ENTER ACCOUNT NUMBER(7digits)'))
        if len(str(acc_no))!=7:
            print("ENTER ACCOUNT NUMBER WITH EXACTY 7 DIGITS")
            continue
        else:
         customer_name=input("ENTER ACCOUNT HOLDER'S NAME").title()
        found=False
        acc={
         'ACCOUNT NUMBER':acc_no,
         'ACCOUNT HOLDER':customer_name,
         'BALANCE':0
        }
        for existing_acc in accounts:
         if existing_acc['ACCOUNT NUMBER']==acc_no:
            found=True
            break
        if found:
            print("ACCOUNT NUMBER ALREADY EXISTS")
            print('ENTER DIFFERENT ACCOUNT NUMBER')
            continue
        else:
          accounts.append(acc)
          print('ACCOUNT CREATED SUCCESSFULLY')
          break
      except ValueError:
          print("ENTER VALID VALUE")
          continue

# view accounts function
def view_acc():
    if not accounts:
            print("THERE ARE CURRENTLY NO ACCOUNTS IN SYSTEM")
    else:
        for acc in accounts:
         print('='*35)
         print(f"ACCOUNT NUMBER: {acc['ACCOUNT NUMBER']}")
         print(f"ACCOUNT HOLDER'S NAME: {acc['ACCOUNT HOLDER']}")
         print(f"ACCOUNT BALANCE: Rs. {acc['BALANCE']}")
         print('='*35)
        print(f"\nTOTAL ACCOUNTS: {len(accounts)}")

# search account function
def search_acc():
    try:
         found=False
         user=int(input("ENTER ACCOUNT NUMBER: "))
         for existing_acc in accounts:
            if existing_acc['ACCOUNT NUMBER']==user:
                found=True
                print('='*35)
                print(f"ACCOUNT NUMBER: {existing_acc['ACCOUNT NUMBER']}")
                print(f"ACCOUNT HOLDER'S NAME: {existing_acc['ACCOUNT HOLDER']}")
                print(f"ACCOUNT BALANCE: Rs. {existing_acc['BALANCE']}")
                print('='*35)
                break
         if not found:
            print("ACCOUNT NOT FOUND")

            
    except ValueError:
        print("ENTER A VALID ACCOUNT NUMBER")


# deposit money function
def deposit():
    try:
        found=False
        
        user=int(input("ENTER ACCOUNT NUMBER"))
        for existing_acc in accounts:
            if existing_acc['ACCOUNT NUMBER']==user:
                found=True
                while True:
                    amount=int(input("ENTER AMOUNT TO BE DEPOSITED: "))
                    if amount>0:
                     existing_acc['BALANCE']+=amount
                     print(f"Rs. {amount} DEPOSITED SUCCESSFULLY")
                     print(f"NEW BALANCE IS Rs. {existing_acc['BALANCE']}")
                     break
                     
                    else:
                     print("ENTER A VALID AMOUNT TO DEPOSIT") 
                     continue
                break             
        if not found:
            print("ACCOUNT NOT FOUND")   
    except ValueError:
        print("PLEASE ENTER VALID VALUE")

# withdraw money function
def withdraw():
    try:
        found=False
            
        user=int(input("ENTER ACCOUNT NUMBER"))
        for existing_acc in accounts:
            if existing_acc['ACCOUNT NUMBER']==user:
                found=True
                while True:
                    amount=int(input("ENTER AMOUNT TO withdraw: "))
                    if amount>0:
                        if amount<=existing_acc['BALANCE']:
                         existing_acc['BALANCE']-=amount
                         print(f"Rs. {amount} withdrawn SUCCESSFULLY")
                         print(f"NEW BALANCE IS Rs. {existing_acc['BALANCE']}")
                         break
                        else:
                            print("INSUFFICIENT BALANCE")
                            continue
                    else:
                        print("ENTER A VALID AMOUNT TO WITHDRAW") 
                        continue
                break             
        if not found:
            print("ACCOUNT NOT FOUND")   
    except ValueError:
        print("PLEASE ENTER VALID VALUE")
        
# view balance function
def view_balance():
    try:
        found=False
        user=int(input("ENTER ACCOUNT NUMBER: "))
        for existing_acc in accounts:
            if existing_acc["ACCOUNT NUMBER"]==user:
                found=True
                print(f"BALANCE IS Rs. {existing_acc['BALANCE']}")
                break
        if not found:
            print("ACCOUNT NOT FOUND")
    except ValueError:
        print("ENTER VALID VALUE")
        
# transfer money function
def money_transfer():
    try:
        found_sender=False
        found_receiver=False
        sender=int(input("ENTER SENDER'S ACCOUNT NUMBER"))
        for sender_acc in accounts:
            if sender_acc['ACCOUNT NUMBER']==sender:
                found_sender=True            
                print("SENDER'S ACCOUNT")
                print('='*35)
                print(f"ACCOUNT NUMBER: {sender_acc['ACCOUNT NUMBER']}")
                print(f"ACCOUNT HOLDER'S NAME: {sender_acc['ACCOUNT HOLDER']}")
                print(f"ACCOUNT BALANCE: Rs. {sender_acc['BALANCE']}")
                print('='*35)
                break
        if not found_sender:
            print('ACCOUNT NOT FOUND')
            return
        receiver=int(input("ENTER RECIVER'S ACCOUNT NUMBER"))
        if receiver==sender:
            print("CANNOT TRANSFER TO THE SAME ACCOUNT")
            return
        for receiver_acc in accounts:
            if receiver_acc['ACCOUNT NUMBER']==receiver:
                found_receiver=True 
                print("RECIVER'S ACCOUNT")
                print('='*35)
                print(f"ACCOUNT NUMBER: {receiver_acc['ACCOUNT NUMBER']}")
                print(f"ACCOUNT HOLDER'S NAME: {receiver_acc['ACCOUNT HOLDER']}")
                print(f"ACCOUNT BALANCE: Rs. {receiver_acc['BALANCE']}")
                print('='*35)
                break
        if not found_receiver:
            print("RECEIVER'S ACCOUNT NOT FOUND")
            return
    except ValueError:
        print("ENTER VALID VALUE")
    
    while True:
        try:
            amount=int(input("ENTER AMOUNT: "))
            if amount<=0:
                print("ENTER A VALID AMOUNT")
                continue
            if amount>sender_acc['BALANCE']:
                print("INSUFFICIENT BALANCE")
                continue
            else:
                sender_acc['BALANCE']-=amount
                receiver_acc['BALANCE']+=amount
                print(f"Rs. {amount} TRANSFERRED SUCCESSFULLY")
                print("="*35)
                print(f"SENDER'S NEW BALANCE Rs. {sender_acc['BALANCE']}")
                print(f"RECEIVER'S NEW BALANCE Rs. {receiver_acc['BALANCE']}")
                print("="*35)
                break
        except ValueError:
            print("ENTER A VALID AMOUNT")
            
                
        
    
                
        
    

    
        
    
    
        
                  
        

    
        
        
         
        
            
        
   
          
        
            
                
                
        
