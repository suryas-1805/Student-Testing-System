from django import forms
from .models import Student_Details

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student_Details
        exclude = ['score','testing']
        fields = ['name','rollno','contact', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please enter matching passwords.")

        return cleaned_data

    # def save(self, commit=True):
    #     user = super().save(commit=True)
    #     user.set_password(self.cleaned_data["password"])

    #     if commit:
    #         user.save()
    #     return user

