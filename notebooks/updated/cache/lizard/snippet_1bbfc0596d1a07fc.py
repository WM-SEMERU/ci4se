def parse_names(cls, names):
    names = [latex_to_unicode(n) for n in re.split(
        '\\sand\\s(?=[^{}]*(?:\\{|$))', names) if n]
    return names