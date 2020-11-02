pamount = 100
amt = eval(input('Enter the value of amt:'))
try:
    pamount = pamount - amt
    if pamount < 0:
        raise Exception("Insufficient Balance")
    else:
        print(f"Your Balance: {pamount}")

except Exception as e:
    print(f'Warning: {e}')
