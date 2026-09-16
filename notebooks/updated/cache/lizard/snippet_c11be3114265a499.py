def do_list_port(self, line):

    def f(p, args):
        o = p.get()
        for p in o.resources.port:
            print('%s %s %s' % (p.resource_id, p.name, p.number))
    self._request(line, f)