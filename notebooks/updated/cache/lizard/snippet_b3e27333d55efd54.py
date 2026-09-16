def validate_url(self, original_string):
    pieces = urlparse.urlparse(original_string)
    try:
        if self.path_only:
            assert not any([pieces.scheme, pieces.netloc])
            assert pieces.path
        else:
            assert all([pieces.scheme, pieces.netloc])
            valid_chars = set(string.letters + string.digits + ':-_.')
            assert set(pieces.netloc) <= valid_chars
            assert pieces.scheme in ['http', 'https']
    except AssertionError as e:
        raise ArgumentError(self.item_name,
            "The input you've provided is not a valid URL.")
    return pieces