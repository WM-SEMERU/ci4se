def collect(self):
    metrics = {}
    if 'scan' in self.config:
        for ld in os.listdir(self.config['owfs']):
            if '.' in ld:
                self.read_values(ld, self.config['scan'], metrics)
    for oid, files in self.config.iteritems():
        if oid[:3] == 'id:':
            self.read_values(oid[3:], files, metrics)
    for fn, fv in metrics.iteritems():
        self.publish(fn, fv, 2)