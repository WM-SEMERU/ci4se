def clean_username(self):
    try:
        user = get_user_model().objects.get(username__iexact=self.
            cleaned_data['username'])
    except get_user_model().DoesNotExist:
        pass
    else:
        if (userena_settings.USERENA_ACTIVATION_REQUIRED and UserenaSignup.
            objects.filter(user__username__iexact=self.cleaned_data[
            'username']).exclude(activation_key=userena_settings.
            USERENA_ACTIVATED)):
            raise forms.ValidationError(_(
                'This username is already taken but not confirmed. Please check your email for verification steps.'
                ))
        raise forms.ValidationError(_('This username is already taken.'))
    if self.cleaned_data['username'].lower(
        ) in userena_settings.USERENA_FORBIDDEN_USERNAMES:
        raise forms.ValidationError(_('This username is not allowed.'))
    return self.cleaned_data['username']