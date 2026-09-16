def respect_language(language):
    if language:
        prev = translation.get_language()
        translation.activate(language)
        try:
            yield
        finally:
            translation.activate(prev)
    else:
        yield