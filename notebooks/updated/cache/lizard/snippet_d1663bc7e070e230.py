def clean_email(self):
    email = self.cleaned_data.get('email')
    qs = User.objects.exclude(id=self.instance.id).filter(email=email)
    if len(qs) == 0:
        return email
    raise forms.ValidationError(ugettext('This email is already registered'))