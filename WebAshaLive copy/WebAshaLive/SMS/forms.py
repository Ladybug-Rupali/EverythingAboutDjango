from SMS.models import *
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'     # ['name','age']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form_control'
            field.widget.attrs['placeholder']='Enter your '+field.label


class PaymentDetailsForm(forms.ModelForm):
    class Meta:
        model=PaymentDetails
        fields='__all__'


