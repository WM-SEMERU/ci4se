def transform(self, data):
    out = []
    keys = sorted(data.keys())
    for k in keys:
        out.append('%s=%s' % (k, data[k]))
    return '\n'.join(out)