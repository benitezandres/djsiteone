from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=10)
    email = forms.EmailField(required=False,label="Your email")
    message = forms.CharField(widget=forms.Textarea(attrs={'cols':22}),max_length=40)


    def clean_message(self):
        message = self.cleaned_data['message']
        list_msg = message.split()
        print('Num ==>',list_msg)
        if len(list_msg) < 5:
            raise forms.ValidationError("Not enough words, 5 minimun")
        
        return message
        