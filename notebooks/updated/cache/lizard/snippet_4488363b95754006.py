def get_values(text):
    res = re.findall('\\[(.*?)\\]', text)
    values = []
    for r in res:
        if '|' in r:
            params = r.split('|')
            for p in params:
                values.append(p)
        else:
            values.append(r)
    values = [str(v.lower()) for v in values]
    return values