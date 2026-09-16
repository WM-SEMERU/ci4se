def do_request(self, line):

    def f(p, method, params):
        result = p.call(method, params)
        print('RESULT %s' % result)
    self._request(line, f)