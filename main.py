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

         
        
            
        
   
          
        
            
                
                
        
