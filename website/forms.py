from django.forms.widgets import Widget
from django import forms


class EnrollForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Name','class':'enroll-input','id':'nm'}),required=True,label=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Your Email','class':'enroll-input','id':'em'}),required=True,label=False)
    contact = forms.CharField(widget=forms.NumberInput(attrs={'placeholder':'Your Mobile','class':'enroll-input','id':'num'}),required=True,label=False,max_length=10)
    course = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Course','class':'enroll-input','id':'sub'}),required=True,label=False)
    message = forms.CharField(required=True,widget=forms.Textarea(attrs={'placeholder':'Your message here','class':'enroll-message','id':'msg'}),label=False)