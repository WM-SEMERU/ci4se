def clean_username(self):
    username = self.cleaned_data.get('username')
    if username.lower() != slugify(username).lower():
        raise forms.ValidationError(ugettext(
            'Username can only contain letters, numbers, dashes or underscores.'
            ))
    lookup = {'username__iexact': username}
    try:
        User.objects.exclude(id=self.instance.id).get(**lookup)
    except User.DoesNotExist:
        return username
    raise forms.ValidationError(ugettext('This username is already registered')
        )