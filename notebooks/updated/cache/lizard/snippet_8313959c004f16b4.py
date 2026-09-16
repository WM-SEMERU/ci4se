def get_domain(self, identity):
    domain = None
    if identity['email']:
        try:
            domain = identity['email'].split('@')[1]
        except IndexError:
            pass
    return domain