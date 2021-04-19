

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import  HomeLoan
from .emi import HomeLoanEmi
from django.views import View


class HomeLoanView(View):
    form_class=HomeLoan
    initial={'key':'value'}
    template_name='layouts/base.html'

    def get(self,request,*args,**kwargs):
        form = self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        #amount=request.POST.get("amount")
        #rate=request.POST.get("rate")
        #month=request.POST.get("month")
        
        #category=calc.bmi_description(bmi)
        if form.is_valid():

            amount=form.cleaned_data["amount"]
            rate=form.cleaned_data["rate"]
            month=form.cleaned_data["month"]
            emi_cal=HomeLoan()

            output=emi_cal.rate_fun(amount,rate,month)
            #print("output",output)
            
            return render(request,self.template_name,{'form':form})
        else:
            return render(request,self.template_name,{'form':form})











    """def home_loan(request):
        form = HomeLoan
        

        return render (request,'layouts/base.html',{'form':form})
        
   

        if request.method =='POST':
            form =HomeLoan(request.POST)
            if form.is_valid():
                amount=form.cleaned_data['amount']
                interest_rate=form.cleaned_data['interest_rate']
                tenure=form.cleaned_data['tenure']

                return HttpResponse("/thakzzz")
        else:

            #form = HomeLoan()

       
    

class BmiView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"calculator/calculator.html",{})
        
    #def post(self,request,*args,**kwargs):
        #print("lllllllllll",args)
        #print("kkkkkk:",**kwargs)
        #print("kkkkkkkkkllmmmmm",request.POST)
        #weight=request.POST.get("weight")
       # height=request.POST.get("height")
        #calc=BmiCalculator()
        #bmi=calc.bmi(height,weight)
        #category=calc.bmi_description(bmi)
        #return render(request,"calculator/calculator.html",{"bmi":bmi,"category":category})


        
        ##template_name = "calculator/calculator.html"
        # """
