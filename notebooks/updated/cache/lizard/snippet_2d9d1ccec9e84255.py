def date(objet):
    if objet:
        return '{}/{}/{}'.format(objet.day, objet.month, objet.year)
    return ''