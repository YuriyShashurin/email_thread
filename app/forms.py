from django import forms
from app.models import Mail

class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ['subject', 'text', 'sender', 'recipient', 'interval']