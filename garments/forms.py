from django import forms
class ContactForm(forms.Form):
        contact_name=forms.CharField(label="Enter your name",required=True)
        contact_email=forms.EmailField(label="Enter email id",required=True)
        content=forms.CharField(label="Your message",required=True,widget=forms.Textarea)