def camel_case_to_underscore(name):
    res = RE_TOKEN1.sub('\\1_\\2', name)
    res = RE_TOKEN2.sub('\\1_\\2', res)
    return res.lower()