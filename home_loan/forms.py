


from django import forms

class HomeLoanForm(forms.Form):
    amount=forms.CharField(label='amount', max_length=100)
    rate=forms.CharField(label='rate', max_length=10)
    month=forms.CharField(label='month', max_length=10)

    