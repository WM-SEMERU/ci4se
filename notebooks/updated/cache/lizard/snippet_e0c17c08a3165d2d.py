def clean(self):
    cleaned_data = super(UserCredential, self).clean()
    if 'username' in cleaned_data and 'password' in cleaned_data:
        auth = utils.import_attr(settings.CAS_AUTH_CLASS)(cleaned_data[
            'username'])
        if auth.test_password(cleaned_data['password']):
            cleaned_data['username'] = auth.username
        else:
            raise forms.ValidationError(_(
                'The credentials you provided cannot be determined to be authentic.'
                ))
    return cleaned_data