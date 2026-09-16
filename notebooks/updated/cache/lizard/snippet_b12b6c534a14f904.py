def unmarshal(self, v):
    if not isinstance(v, datetime):
        if isinstance(v, six.integer_types):
            v = arrow.get(v)
        else:
            try:
                v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%SZ')
            except ValueError:
                v = arrow.get(v).datetime
        v = v.replace(tzinfo=self.tzinfo)
    return v