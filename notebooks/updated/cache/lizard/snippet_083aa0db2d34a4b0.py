def _run_cmd(self, command):
    if self.throttle:
        tables = self.engine.describe_all(False)
        limiter = self.throttle.get_limiter(tables)
    else:
        limiter = None
    self.engine.rate_limit = limiter
    results = self.engine.execute(command)
    if results is None:
        pass
    elif isinstance(results, basestring):
        print(results)
    else:
        with self.display() as ostream:
            formatter = FORMATTERS[self.conf['format']](results, ostream,
                pagesize=self.conf['pagesize'], width=self.conf['width'])
            formatter.display()
    print_count = 0
    total = None
    for cmd_fragment, capacity in self.engine.consumed_capacities:
        total += capacity
        print(cmd_fragment)
        print(indent(str(capacity)))
        print_count += 1
    if print_count > 1:
        print('TOTAL')
        print(indent(str(total)))