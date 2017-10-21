from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        print('yo')
        send_mail(
            'Wedding Contact Form Submission',
            f'Sender: {self.cleaned_data["name"]}\n\nSender Email: {self.cleaned_data["email"]}'
            f'\n\nMessage: \n{self.cleaned_data["message"]}',
            settings.DEFAULT_FROM_EMAIL,
            settings.CONTACT_FORM_RECIPIENT_LIST,
            fail_silently=False,
        )
        pass