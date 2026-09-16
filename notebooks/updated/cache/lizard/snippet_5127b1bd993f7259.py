def render(value):
    if not value:
        return '^$'
    if value[0] != beginning:
        value = beginning + value
    if value[-1] != end:
        value += end
    return value