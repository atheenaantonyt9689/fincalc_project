#from django .forms import ModelForm
""""from django import forms 

from .models import HomeLoan
#class HomeLoanForm(forms.Form):
    #amount=forms.CharField()
    #interest_rate=forms.CharField()
    #tenure=forms.CharField()

class HomeLoanForm(forms.ModelForm):
    class Meta:
        model=HomeLoan
        fields=['amount', 'interest_rate', 'tenure']
#template_name='layouts/base.html'"""



from django import forms

class HomeLoan(forms.Form):
    amount=forms.CharField(label='amount', max_length=100)
    interest_rate=forms.CharField(label='rate', max_length=10)
    tenure=forms.CharField(label='month', max_length=10)

    