from BankAccount import *
import sys
def options(i):
    choices = {
        1 : 'Deposit',
        2 : 'Withdrawal',
        3 : 'Balance Enquiry',
        4 : 'Exit'
    }

    return choices.get(i, "Invalid option")
def banktransactions():
    restart = "yes"
    bc = BankAccount()
    while restart[0] == "y" or restart[0] == "Y":
        print("\n\t1. Deposit\n\t2. Withdrawal\n\t3. Balance Enquiry\n\t4. Exit")
        ch = eval(input("Select an option:"))
        option = options(ch)
        
        if option == "Deposit":
            amt = eval(input("Enter the amount to be credited:"))
            msg ,amnt = bc.deposit(amt)
            print("{0}}\n Your Balance:{1}".format(msg,amnt))
            restart = input("Do you want to continue Press(Yes/No):")
            
        elif option == "Withdrawal":
            amt = eval(input("Enter the amount to be debited:"))
            msg, amnt = bc.withdrawal(amt)
            if msg != "I" or msg != "i":
                print("\n\tYour Balance:{0}".format(amnt))
                restart = input("Do you want to continue Press(Yes/No):")
            else:
                print("{0}\n Your Balance:{1}".format(msg,amnt))
                restart = input("Do you want to continue Press(Yes/No):")
                
        elif option == "Balance Enquiry":
            amnt = bc.getBalanceEnquiry()
            print("Your Balance:",amnt)
            restart = input("Do you want to continue Press(Yes/No):")
            
        elif option == "Exit":
            sys.exit()

def main():
    restart = True
    while restart:
        uname = input("Enter the username:")
        paswd = input("Enter the password:")
        bc = BankAccount()
        msg = bc.login(uname,paswd)
        if msg[0] == "L" or msg[0] == "l":
            print(msg)
            restart = False
            banktransactions()
        else:
            print(msg)



if __name__ == '__main__':
    main()