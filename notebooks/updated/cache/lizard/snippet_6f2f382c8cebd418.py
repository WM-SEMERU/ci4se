def fail(self, msg, lineno=None, exc=TemplateSyntaxError):
    if lineno is None:
        lineno = self.stream.current.lineno
    raise exc(msg, lineno, self.name, self.filename)