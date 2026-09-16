def _ReverseHostname(self, hostname):
    if not hostname:
        return ''
    if len(hostname) <= 1:
        return hostname
    if hostname[-1] == '.':
        return hostname[::-1][1:]
    return hostname[::-1][0:]