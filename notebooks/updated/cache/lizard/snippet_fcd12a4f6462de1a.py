def save(self, **kwargs):
    try:
        return super().save(**kwargs)
    except SlugError as error:
        raise ParseError(error)