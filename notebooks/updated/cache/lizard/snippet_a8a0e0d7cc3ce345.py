def is_valid_mimetype(response):
    blacklist = ['image/']
    mimetype = response.get('mimeType')
    if not mimetype:
        return True
    for bw in blacklist:
        if bw in mimetype:
            return False
    return True