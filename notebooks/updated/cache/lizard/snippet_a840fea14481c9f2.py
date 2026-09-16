def images(language, word, n=20, *args, **kwargs):
    from lltk.images import google
    return google(language, word, n, *args, **kwargs)