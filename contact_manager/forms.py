# contact_manager/forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone']
        # You can customize the form further by adding widgets, labels, etc.

    # If you need additional form validation or customization, you can add methods here.
