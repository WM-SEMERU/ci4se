def username_validator(self, form, field):
    username = field.data
    if len(username) < 3:
        raise ValidationError(_('Username must be at least 3 characters long'))
    valid_chars = (
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._')
    chars = list(username)
    for char in chars:
        if char not in valid_chars:
            raise ValidationError(_(
                "Username may only contain letters, numbers, '-', '.' and '_'")
                )