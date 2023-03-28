from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# refer to django registration for this
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # dont forget to add names
        fields = ("username", "email", "password1", "password2") 

#saving the form
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"] #still do not quite understand
        if commit:
            user.save()
        return user