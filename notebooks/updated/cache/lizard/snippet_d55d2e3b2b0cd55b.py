def slugify(value, allow_unicode=False):
    value
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore'
            ).decode('ascii')
    value = re.sub('[^\\w\\s-]', '', value).strip().lower()
    return re.sub('[-\\s]+', '-', value)