def _make_fits(self):
    a = self.tests[self.active]
    args = self.curargs
    if len(args['fits']) > 0:
        for fit in list(args['fits'].keys()):
            a.fit(args['independent'], fit, args['fits'][fit], args[
                'threshold'], args['functions'])