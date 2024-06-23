from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from book.models import Item

class SignInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class AddToCartForm(forms.Form):
    item = forms.ModelChoiceField(queryset=Item.objects.all(), empty_label=None)
    quantity = forms.IntegerField(min_value=1)        