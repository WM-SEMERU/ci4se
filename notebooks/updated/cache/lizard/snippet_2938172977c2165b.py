def parse_expression(self, expr):
    m = re.match('^(.*?(?:::)?(?:operator)?)((?:::[^:]*|[^:]*)?)$', expr)
    prefix = m.group(1)
    tail = m.group(2)
    return [prefix, tail]