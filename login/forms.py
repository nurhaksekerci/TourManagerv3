from django import forms
from django.contrib.auth.models import User
from company.models import *

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True}), label='Password')
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'required': True}), label='Confirm Password')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data


class PasswordResetForm(forms.Form):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Phone Number', 
        'required': True
    }), label='Phone Number')


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name',
            'city',
            'district',
            'neighborhood',
            'address',
            'complete_at',
            'branch',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'district': forms.Select(attrs={'class': 'form-control'}),
            'neighborhood': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'complete_at': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'branch': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Name',
            'city': 'City',
            'district': 'District',
            'neighborhood': 'Neighborhood',
            'address': 'Address',
            'complete_at': 'Complete Date',
            'branch': 'Branch',
        }

    def clean_branch(self):
        branch = self.cleaned_data.get('branch')
        if branch < 1:
            raise forms.ValidationError("Branch must be a positive integer.")
        return branch

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = [
            'company',
            'name',
            'city',
            'district',
            'neighborhood',
            'address',
        ]
        widgets = {
            'company': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'district': forms.Select(attrs={'class': 'form-control'}),
            'neighborhood': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'company': 'Company',
            'name': 'Name',
            'city': 'City',
            'district': 'District',
            'neighborhood': 'Neighborhood',
            'address': 'Address',
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Name is required.")
        return name
