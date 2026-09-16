def _unknown_args(self, args):
    for u in args:
        self.tcex.log.warning('Unsupported arg found ({}).'.format(u))