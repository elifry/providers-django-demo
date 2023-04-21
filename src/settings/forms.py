from django import forms

# creating a form
class NotificationsForm(forms.Form):
    # specify fields for model
    email = forms.CharField()
    phone = forms.CharField(max_length=12)

    def clean_email(self):
        email = self.cleaned_data['email']
        if 'connect' not in email:
            raise forms.ValidationError('Sorry, email is invalid.')
        return email
