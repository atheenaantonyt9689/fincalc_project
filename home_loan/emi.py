
class EmiCalculator:
    def __init__(self,amount,rate,month):
        self.amount=amount
        self.rate=rate
        self.month=month
    def emi(self):
        
        rate=float(self.rate)/int(self.month)*100
        x=float(rate)
        total_rate=rate*int(self.month)
        emi=(int(self.amount)*x*(1+x)**int(self.month))/(((1+x)**int(self.month))-1)
        return emi
    def total_amount(self):
        return self.emi()*int(self.month)
    def interest(self):
        return self.total_amount()-int(self.amount)





    #def rate_fun(self,amount,rate,month):
        #rate=float(rate)/int(month)*100
        #x=float(rate)
        #total_rate=x* int(month)
        #emi=(int(amount)*float(x)*(1+float(x))**(int(month)))/(((1+float(x))**int(month))-1)
        #total_amount_payable=float(emi)+total_rate
        #return emi"""


