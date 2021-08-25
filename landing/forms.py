from django import forms
from captcha.fields import CaptchaField
from django.contrib import messages

from landing.models import Order


class OrderForm(forms.Form):
    name_form = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'id': 'fname'}))
    phone_form = forms.CharField(max_length=20,
                                 widget=forms.TextInput(
                                     attrs={'id': 'phone', 'type': 'tel', 'name': 'phone',
                                            'data-tel-input': 'data-tel-input'}))
    email_form = forms.CharField(widget=forms.EmailInput(attrs={'id': 'email'}))
    organization_name_form = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'id': 'orgname'}))
    organization_address_form = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'id': 'orgadres'}))
    count_images_form = forms.CharField(max_length=200, widget=forms.NumberInput(attrs={'id': 'count'}))
    captcha = CaptchaField(label='Are you an human? ')


    def form_invalid(self, form):
        messages.error(self.request, form.non_field_errors())
        return super().form_invalid(form)
