def from_urlencode(self, data, options=None):
    qs = dict((k, v if len(v) > 1 else v[0]) for k, v in urlparse.parse_qs(
        data).iteritems())
    return qs