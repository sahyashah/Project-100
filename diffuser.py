class ATM(object):
    def __init__(self,pinnumber,cardnumber):
        self.pinnumber=pinnumber
        self.cardnumber=cardnumber
        

    def cashWidthdrawl(self):
        print ('cash has benn withdrawn')
    
    def BalanceEnquiry(self):
        print('This is your account balance:0')

ATM1=ATM('4231','864554274837')
print(ATM1.cashWidthdrawl())