from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label='Email Address', required=True,\
        error_messages={'required':'Would need ur email','invalid': 'Hey, enter right format email'})
    mobile = forms.CharField(label='Mobile Number', required=False, max_length=10, min_length=8)
    message = forms.CharField(required=True, widget=forms.Textarea, max_length=100,\
        error_messages={'required': 'We need to hear from u!'})

    # custom validation
    def clean_message(self):
        message = self.cleaned_data['message']
        words = message.split(' ')
        if len(words) < 10:
            raise forms.ValidationError('Please be elaborate!')
        return message
