def is_authenticated(self):
    if not self.token:
        return False
    try:
        self.lookup_token()
        return True
    except exceptions.Forbidden:
        return False
    except exceptions.InvalidPath:
        return False
    except exceptions.InvalidRequest:
        return False