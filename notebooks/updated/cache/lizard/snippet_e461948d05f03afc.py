def slugify(string):
    if not string:
        return string
    string = re.sub('[^\\w\\s-]', '', unicodedata.normalize('NFKD',
        de_camel(string, '-')).encode('ascii', 'ignore').decode('ascii')
        ).strip()
    return re.sub('[-_\\s]+', '-', string).strip('-').lower()