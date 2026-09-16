def is_valid(self):
    if not super(ProfileRequestForm, self).is_valid():
        return False
    validity = True
    if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
        form_add_error(self, 'password', "Passwords don't match.")
        form_add_error(self, 'confirm_password', "Passwords don't match.")
        validity = False
    return validity