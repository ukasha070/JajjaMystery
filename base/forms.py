from django import forms
from JaajaMystery.utils import check_for_xss
from django.core.exceptions import ValidationError

input_class_name = "w-full h-12 outline-none outline-transparent px-4 bg-transparent text-neutral-1 border border-neutral-100 dark: border-neutral-800 rounded-xl"

text_area_class_field = "w-full h-fit outline-none outline-transparent p-4 bg-transparent text-neutral-1 border border-neutral-100 dark: border-neutral-800 rounded-xl px-4 py-4"

class MessageForm(forms.Form):
    message = forms.CharField(max_length=500, min_length=10, widget=forms.Textarea(
        attrs={
            "class": text_area_class_field,
            "placeholder": "Message", 
            "rows": 2
        }
    ))
    email = forms.EmailField(max_length=100, min_length=6, widget=forms.EmailInput(
        attrs={
            "class": input_class_name, 
            "placeholder": "Email"
        }
    ))
    full_name = forms.CharField(max_length=20, min_length=4, widget=forms.TextInput(
                attrs={
                        "class": input_class_name, 
                        "placeholder": "Full Name",
                    }
                ))
    location = forms.CharField(max_length=50, min_length=4, widget=forms.TextInput(
                attrs={
                    "class": input_class_name, 
                    "placeholder": "Location",
                    }
                ))
    tell_phone = forms.CharField(max_length=15, min_length=5, widget=forms.NumberInput(
        attrs={
            "class": input_class_name, 
            "placeholder": "Phone",
            }
        ))


    def clean_email(self):
        data = self.cleaned_data["email"]
        if check_for_xss(data):
            return data
        else:
            raise ValidationError("Field contains xss")
        
    def clean_message(self):
        data = self.cleaned_data["message"]
        if check_for_xss(data):
            return data
        else:
            raise ValidationError("Field contains xss")

    def clean_full_name(self):
        full_name = self.cleaned_data["full_name"]
        if check_for_xss(full_name):
            return full_name
        else:
            raise ValidationError("Field contains xss")

    def clean_location(self):
        data = self.cleaned_data["location"]
        if check_for_xss(data):
            return data
        else:
            raise ValidationError("Field contains xss")
      
    def clean_tell_phone(self):
        data = self.cleaned_data["tell_phone"]
        if check_for_xss(data):
            return data
        else:
            raise ValidationError("Field contains xss")
    
