class MyError(Exception):
    def __init__(self):
        self.msg = 'Insufficient Fund'

    def __str__(self):
        return self.msg

class BankAccount:
    def __init__(self):
        self.amount = 10000.0

    def getBalanceEnquiry(self):
        return self.amount

    def withdrawal(self, amnt):
        try:
            if (self.amount - amnt) <= 0 or (self.amount - amnt) <= 500:
                raise (MyError())
            else:
                self.amount = self.amount - amnt
                msg = "Amount Debited"
                return msg,self.amount
        except MyError as err:
            print("Exception Occured : ",err.msg)
            return err.msg, self.amount


    def deposit(self,amnt):
        self.amount = self.amount + amnt
        msg = "Amount Credited"
        return msg, self.amount

    def login(self,uname,passwd):
        if  uname == 'Bank':
            if  passwd == 'Bank@123':
                msg = "Logged in successfully"
            else:
                msg = "Password Mismatch"
        else:
            msg = "Invalid username"
        return msg


