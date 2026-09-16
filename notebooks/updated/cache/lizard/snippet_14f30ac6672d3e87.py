def user_parse(data):
    for email in data.get('emails', []):
        if email.get('primary'):
            yield 'id', email.get('email')
            yield 'email', email.get('email')
            break