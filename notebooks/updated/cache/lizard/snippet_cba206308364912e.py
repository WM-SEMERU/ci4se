def prompt(msg, default=NO_DEFAULT, validate=None):
    while True:
        response = input(msg + ' ').strip()
        if not response:
            if default is NO_DEFAULT:
                continue
            return default
        if validate is None or validate(response):
            return response