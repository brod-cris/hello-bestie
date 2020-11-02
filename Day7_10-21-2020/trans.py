import sys

uname = input('Enter the Username:')
pswd = input('Enter the password:')
if uname == 'Bank':
    if pswd == "Bank@123":
        print(f'Welcome : {uname}, You logged in successfully!')
        print('Please select your choice.')
    else:
        print('Password Mismatch')
        sys.exit()
else:
    print('Invalid Username')
    sys.exit()


def my_choices(ch):
    my_dict = {
        1: "Deposit",
        2: "Withdrawal",
        3: "Balance Enquiry",
        4: "Exit"
    }

    return my_dict.get(ch, "Invalid Option")


if __name__ == "__main__":
    restart = "yes"
    while restart[0] == "y" or restart[0] == "Y":
        print('1. Deposit\n2. Withdrawal\n3. Balance Enquiry \n4. Exit\n Select an option:')
        ch = eval(input())
        options = my_choices(ch)
        if options == "Deposit":
            print('Welcome Bank')
            a = 10000
            b = eval(input('Enter an amount to be deposited:'))
            print(f"Your current Account Balance: {a} + {b} = ${a+b}")
            restart = input('Do you want to continue? Press (Yes/No):')

        elif options == "Withdrawal":
            print('Welcome Bank')
            a = 10000
            b = eval(input('Enter an amount to be withdrawn:'))
            print(f"Your current Account Balance: {a} - {b} = ${a-b}")
            restart = input('Do you want to continue? Press (Yes/No):')

        elif options == "Balance Enquiry":
            print('Welcome Bank')
            a = 10000
            print(f"Your current Account Balance: ${a}")
            restart = input('Do you want to continue? Press (Yes/No):')

        elif options == "Exit":
            print('Have a nice day!')
            sys.exit()

        else:
            print(f'Warning: {options}')
            restart = input('Do you want to continue? Press (Yes/No):')
