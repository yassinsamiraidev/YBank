from Accounts import accounts
import pyinputplus as pi

start = True

print('='*40)
print('   🏦 YASSIN BANK SYSTEM')
print('='*40)
while start == True:
    print('Choose:\n    1-Create An Account\n    2-Delete An Account\n    3-Add Money\n    4-Withdraw Money\n    5-Know Balance\n    6-Activate Account\n    7-Deactivate Account\n    8-Transfer Money \n    9-Quit')
    choice = pi.inputInt('Enter Your Choice: ',min=1,max=9)
    if choice == 1:
        name = pi.inputStr("Enter Your Name: ")
        password = pi.inputStr('Enter 8 digit PIN: ',allowRegexes=[r'^\d{8}$'],blockRegexes=[r'[a-zA-Z]',r'[^0-9]',r'^\d{1,7}$',r'^\d{9,}$'])
        balance = pi.inputInt("Enter Your Balance: ")
        account = accounts(name,password,None,balance,True)
        account.create()
    elif choice == 2:
        id = pi.inputStr("Enter Your id: ")
        password = pi.inputStr('Enter 8 digit PIN: ',allowRegexes=[r'^\d{8}$'],blockRegexes=[r'[a-zA-Z]',r'[^0-9]',r'^\d{1,7}$',r'^\d{9,}$'])
        account = accounts(None,password,id,None,None)
        account.delete()
    elif choice == 3:
        id = pi.inputStr("Enter Your id: ")
        password = pi.inputStr('Enter 8 digit PIN: ',allowRegexes=[r'^\d{8}$'],blockRegexes=[r'[a-zA-Z]',r'[^0-9]',r'^\d{1,7}$',r'^\d{9,}$'])
        balance = pi.inputInt("Enter Your Money: ")
        account = accounts(None,password,id,balance,True)
        account.add()
    elif choice == 4:
        id = pi.inputStr("Enter Your id: ")
        password = pi.inputStr('Enter 8 digit PIN: ',allowRegexes=[r'^\d{8}$'],blockRegexes=[r'[a-zA-Z]',r'[^0-9]',r'^\d{1,7}$',r'^\d{9,}$'])
        balance = pi.inputInt("Enter Your Money: ")
        account = accounts(None,password,id,balance,True)
        account.withdraw()
    elif choice == 5:
        id = pi.inputStr("Enter Your id: ")
        password = pi.inputStr('Enter 8 digit PIN: ',allowRegexes=[r'^\d{8}$'],blockRegexes=[r'[a-zA-Z]',r'[^0-9]',r'^\d{1,7}$',r'^\d{9,}$'])
        account = accounts(None,password,id,None,True)
        account.Balance()
    elif choice == 6:
        id = pi.inputStr("Enter Your id: ")
        password = pi.inputStr('Enter 8 digit PIN: ',allowRegexes=[r'^\d{8}$'],blockRegexes=[r'[a-zA-Z]',r'[^0-9]',r'^\d{1,7}$',r'^\d{9,}$'])
        account = accounts(None,password,id,None,True)
        account.activate()
    elif choice == 7:
        id = pi.inputStr("Enter Your id: ")
        password = pi.inputStr('Enter 8 digit PIN: ',allowRegexes=[r'^\d{8}$'],blockRegexes=[r'[a-zA-Z]',r'[^0-9]',r'^\d{1,7}$',r'^\d{9,}$'])
        account = accounts(None,password,id,None,True)
        account.deactivate()
    elif choice == 8:
        id = pi.inputStr("Enter Your id: ")
        password = pi.inputStr('Enter 8 digit PIN: ',allowRegexes=[r'^\d{8}$'],blockRegexes=[r'[a-zA-Z]',r'[^0-9]',r'^\d{1,7}$',r'^\d{9,}$'])
        new_id = pi.inputStr("Enter the id to transfer money to: ")
        balance = pi.inputInt("Enter Your Money: ")
        account = accounts(None,password,id,balance,True)
        account.transfer(str(new_id))
    elif choice == 9:
        print("Bye !")
        break