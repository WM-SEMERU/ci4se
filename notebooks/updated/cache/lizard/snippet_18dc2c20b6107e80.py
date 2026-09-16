def validate(self, value, model=None, context=None):
    regex = self.regex()
    match = regex.match(value)
    if not match:
        return Error(self.not_email)
    return Error()