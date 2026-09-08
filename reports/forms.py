from django import forms
from django.contrib.auth.models import User
from .models import Report

class register(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput
    ) 
    password_confirm = forms.CharField(
        widget=forms.PasswordInput
    )
    class Meta:
        model = User
        fields = ['username','email','password']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if User.objects.filter(username = username ).exists():
            raise forms.ValidationError("The username is alreay taken.")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        
        
        return cleaned_data

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [ 
                    'item_name',
                    'report_type',
                    'category',
                    'description',
                    'location',
                    'date',
                    'contact_info',
                    'image',
                ]
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
        }
        
