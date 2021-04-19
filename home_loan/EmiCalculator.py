
class HomeLoanEmi:
    def rate_fun(self,amount,rate,month):
        rate=rate/month*100
        x=float(rate)
        total_rate=rate*month
        emi=(amount*x*(1+x)**month)/(((1+x)**month)-1)
        total_amount_payable=emi+total_rate
        #print("rate",rate)
        #print("total_rate",total_rate)
        #print("_emi",emi)
        #print("total payable amount:",total_amount_payable)
        return emi

#obj1=HomeLoan()
#x=obj1.rate_fun(1000,10,12)
#b=obj1.emi(5000,10,12,x)

