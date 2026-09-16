def do_get_queue_config(self, line):

    def f(p, args):
        try:
            source, queue = args
        except:
            print('argument error')
            return
        o = p.get_config(source)
        for q in o.resources.queue:
            if q.resource_id != queue:
                continue
            print(q.resource_id)
            conf = q.properties
            for k in self._queue_settings:
                try:
                    v = getattr(conf, k)
                except AttributeError:
                    continue
                print('%s %s' % (k, v))
    self._request(line, f)