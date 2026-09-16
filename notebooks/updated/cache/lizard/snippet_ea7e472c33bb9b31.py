def get_uri(self, image):
    image = image or ''
    uri = ''
    match = re.match('^(?P<uri>.+)://', image)
    if match:
        uri = match.group('uri')
    return uri