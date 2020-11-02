import sys

uname = input('Enter the Username:')
pswd = input('Enter the password:')
if uname == 'Bank':
    if pswd == "Bank@123":
        print(f'Welcome : {uname}, You logged in successfully')
    else:
        print('Password Mismatch')
else:
    print('Invalid Username')
    sys.exit()
