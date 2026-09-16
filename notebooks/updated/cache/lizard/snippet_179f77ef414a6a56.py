def urlencode(query):
    if hasattr(urllib, 'parse'):
        return urllib.parse.urlencode(query)
    else:
        return urllib.urlencode(query)