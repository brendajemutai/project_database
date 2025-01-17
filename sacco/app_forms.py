from django import forms

from sacco.models import Customer, Deposit

GENDER_CHOICES = { "male": "Male", "female": "Female",}

class CustomerForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'dob', 'weight', 'gender']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'min': '1980-01-01-', 'max': '2005-01-01'}),
            'weight': forms.NumberInput(attrs={'type': 'number', 'min': '35', 'max': '100'}),
        }
class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'type': 'number', 'min': '0', 'max': '100000'}),
        }

# Update Customer/ Gender radio button
# Cloning and setting up the virtual env