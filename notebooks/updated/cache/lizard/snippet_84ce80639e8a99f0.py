def mdstrip(value, length=None, end='…'):
    if not value:
        return ''
    if EXCERPT_TOKEN in value:
        value = value.split(EXCERPT_TOKEN, 1)[0]
    rendered = md(value, wrap=False)
    text = do_striptags(rendered)
    text = bleach_clean(text)
    if length and length > 0:
        text = do_truncate(None, text, length, end=end, leeway=2)
    return text