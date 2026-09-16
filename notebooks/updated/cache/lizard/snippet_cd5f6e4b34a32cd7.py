def duplicate(self, name):
    dup = self.make_request(method='update', raw_result=True, resource=
        'duplicate', params={'name': name})
    return type(self)(name=name, href=dup.href, type=type(self).typeof)