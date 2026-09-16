def update(self, argv):
    if len(argv) == 0:
        error('Command requires an index name', 2)
    name = argv[0]
    if name not in self.service.indexes:
        error("Index '%s' does not exist" % name, 2)
    index = self.service.indexes[name]
    fields = self.service.indexes.itemmeta().fields.optional
    rules = dict([(field, {'flags': ['--%s' % field]}) for field in fields])
    opts = cmdline(argv, rules)
    index.update(**opts.kwargs)