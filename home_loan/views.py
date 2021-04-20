

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import  HomeLoanForm
from .emi import EmiCalculator
from django.views import View
from .models import HomeLoan


class HomeLoanView(View):
    form_class=HomeLoanForm
    initial={'key':'value'}
    template_name='layouts/base.html'

    def get(self,request,*args,**kwargs):
        form = self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
                
        if form.is_valid():

            amount=form.cleaned_data["amount"]
            rate=form.cleaned_data["rate"]
            month=form.cleaned_data["month"]
            #total_amount_payable=form.cleaned_data["total_amount_payable"]
            calc=EmiCalculator(amount,rate,month)           
            
            context={'emi':calc.emi(),
            'total_amount':calc.total_amount(),
            'interest':calc.interest()


            }

            loan=HomeLoan.objects.create(amount=amount,rate=rate,month=month)

            loan.save()

        return render (request,self.template_name ,context)

            
            #return render(request,self.template_name,context)
        #else:
            #return render(request,self.template_name,{'form':form})











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
