def sub_macros(string, base_url):
    macros = {'|url|': base_url, '|media|': os.path.join(base_url, 'media'),
        '|page|': os.path.join(base_url, 'page')}
    for key, val in macros.items():
        string = string.replace(key, val)
    return string