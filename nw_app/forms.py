from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 50,required=True)
    email = forms.EmailField(max_length = 30,required=True)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length = 750)