class ContactForm(forms.Form):
    fio = forms.CharField(max_length=200)
    email = forms.EmailField()
    city = forms.CharField(max_length=200, required=False)
    phone = forms.CharField(max_length=12, required=False)
    agree = froms.BooleanField(required=False)
    content = forms.CharField(widget=forms.Textarea)
