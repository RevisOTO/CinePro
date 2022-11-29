from django.forms import ModelForm,EmailInput,forms
from gestorapp.models import *

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'email':EmailInput(attrs={'type':'email'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
            'registered_on': forms.DateTimeField(attrs={'class':'form-control','initial':datetime.datetime.now()})
        }