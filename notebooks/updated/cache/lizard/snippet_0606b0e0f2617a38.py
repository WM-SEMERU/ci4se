def is_url(str_):
    return any([str_.startswith('http://'), str_.startswith('https://'),
        str_.startswith('www.'), '.org/' in str_, '.com/' in str_])