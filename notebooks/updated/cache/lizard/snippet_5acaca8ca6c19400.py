def _add_scheme():
    lists = [urllib.parse.uses_relative, urllib.parse.uses_netloc, urllib.
        parse.uses_query]
    for l in lists:
        l.append('mongodb')