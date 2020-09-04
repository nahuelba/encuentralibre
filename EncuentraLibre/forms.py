# make sure this is at the top if it isn't already
from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input is-medium'}), required=True)
    contact_email = forms.EmailField(widget=forms.TextInput(attrs={'class':'input is-medium'}), required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(
        attrs={'class':'textarea is-medium'})
        
    )