def password_validator(self, form, field):
    password = list(field.data)
    password_length = len(password)
    lowers = uppers = digits = 0
    for ch in password:
        if ch.islower():
            lowers += 1
        if ch.isupper():
            uppers += 1
        if ch.isdigit():
            digits += 1
    is_valid = password_length >= 6 and lowers and uppers and digits
    if not is_valid:
        raise ValidationError(_(
            'Password must have at least 6 characters with one lowercase letter, one uppercase letter and one number'
            ))