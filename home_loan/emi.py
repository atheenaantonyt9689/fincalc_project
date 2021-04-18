"""class HomeLoan:
    def rate_fun(self,rate,month):
        rate=rate/month*100
        total_rate=rate*month
        print("total_rate",total_rate)
        return rate

    def emi(self,P,R,N,x):
        print("p",P)
        loan=int(P)     
        rate=R
        month=int(N)          
        print("x",x)
        #emi=(loan*x*((1+x)**month)/((1+x)**month)-1)
        
        emi=(loan*x*(1+x)**12)/((1+x)**12)-1
        #Emi=(loan*float(rate)*(1+float(rate)/100*month)**month)/(1+(float(rate)/100*month)**month)-1
        return emi
    

obj1=HomeLoan()
x=obj1.rate_fun(10,12)
b=obj1.emi(5000,10,12,x)

print("interst",x)
print("emi:",b)"""

class HomeLoan:
    def rate_fun(self,amount,rate,month):
        rate=rate/month*100
        x=float(rate)
        total_rate=rate*month
        emi=(amount*x*(1+x)**12)/((1+x)**12)-1
        total_amount_payable=emi+total_rate
        #print("rate",rate)
        #print("total_rate",total_rate)
        #print("_emi",emi)
        #print("total payable amount:",total_amount_payable)
        return emi
