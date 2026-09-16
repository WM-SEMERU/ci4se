def get(self, url_type):
    lowtype = url_type.lower()
    if lowtype == 'public':
        return self.public_url
    elif lowtype == 'private':
        return self.private_url
    else:
        raise ValueError(
            "Valid values are 'public' or 'private'; received '%s'." % url_type
            )