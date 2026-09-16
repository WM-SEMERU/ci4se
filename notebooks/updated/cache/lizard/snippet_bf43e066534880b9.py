def get_version(self):
    if not self.node.version:
        return None
    try:
        version = smart_str('%s' % self.node.version.resolve(self.context))
    except template.VariableDoesNotExist:
        raise template.TemplateSyntaxError(
            '"%s" tag got an unknown variable: %r' % (self.node.nodename,
            self.node.version.var))
    return '%s' % version