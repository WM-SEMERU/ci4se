def get_message(self, method, args, kwargs, options=None):
    content = self.headercontent(method, options=options)
    header = self.header(content)
    content = self.bodycontent(method, args, kwargs)
    body = self.body(content)
    env = self.envelope(header, body)
    if self.options().prefixes:
        body.normalizePrefixes()
        env.promotePrefixes()
    else:
        env.refitPrefixes()
    return Document(env)