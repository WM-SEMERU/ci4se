def clean_key(self):
    key = self.cleaned_data['key']
    gpg = GPG(gnupghome=GNUPG_HOME)
    result = gpg.import_keys(key)
    if result.count == 0:
        raise forms.ValidationError(_('Invalid Key'))
    return key