def _match_path(self, environ):
    path = environ['PATH_INFO'] or '/'
    match = self.static.get(path)
    if match:
        return match, {}
    for combined, rules in self.dynamic:
        match = combined.match(path)
        if not match:
            continue
        gpat, match = rules[match.lastindex - 1]
        return match, gpat.match(path).groupdict() if gpat else {}
    if self.static or self.dynamic or not self.routes:
        return None, {}
    if not environ.get('wsgi.run_once'):
        self._compile()
        return self._match_path(environ)
    epath = path.replace(':', '\\:')
    match = self.routes.get(epath)
    if match:
        return match, {}
    for rule in self.rules:
        if rule.count(':') < rule.count('\\:'):
            continue
        match = self._compile_pattern(rule).match(path)
        if match:
            return self.routes[rule], match.groupdict()
    return None, {}