

from django import forms

from .models import Checkout,Contact


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['name','email','address','city','state','zipcode','country','phone','payment','comments','date']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields=['fname','lname','email','message']
        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'email': 'Email Address',
            'message': 'Message',
        }