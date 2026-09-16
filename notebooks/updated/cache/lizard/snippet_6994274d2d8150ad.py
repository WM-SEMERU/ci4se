def _docf(self, tag, val):
    if tag == 'route':
        if ':' in val:
            val, version = val.split(':', 1)
            version = int(version)
        else:
            version = 1
        url = fmt_url(self.cur_namespace.name, val, version)
        return url[len(self.cur_namespace.name) + 1:]
    return val