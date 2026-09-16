def convert(string, sanitize=False):
    return r.convert(string, preprocess if sanitize else False)