def _run_setup_py(self, args, echo=True, echo2=True, ff=''):
    python = self.python
    if ff:
        setup_py = '-c"%s"' % (RUN_SETUP % locals())
    else:
        setup_py = 'setup.py %s' % ' '.join(args)
    rc, lines = self.process.popen('"%(python)s" %(setup_py)s' % locals(),
        echo=echo, echo2=echo2)
    return rc, lines