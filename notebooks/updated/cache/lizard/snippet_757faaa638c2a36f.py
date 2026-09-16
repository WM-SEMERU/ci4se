def process_op(self, ns, raw):
    docid = self.__get_id(raw)
    op = raw['op']
    if op == 'i':
        self.insert(ns=ns, docid=docid, raw=raw)
    elif op == 'u':
        self.update(ns=ns, docid=docid, raw=raw)
    elif op == 'd':
        self.delete(ns=ns, docid=docid, raw=raw)
    elif op == 'c':
        self.command(ns=ns, raw=raw)
    elif op == 'db':
        self.db_declare(ns=ns, raw=raw)
    elif op == 'n':
        self.noop()
    else:
        logging.error('Unknown op: %r' % op)
    self.ts = raw['ts']