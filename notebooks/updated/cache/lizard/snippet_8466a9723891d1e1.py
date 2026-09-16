def latex_run(self):
    self.log.info('Running %s...' % self.latex_cmd)
    cmd = [self.latex_cmd]
    cmd.extend(LATEX_FLAGS)
    cmd.append('%s.tex' % self.project_name)
    try:
        with open(os.devnull, 'w') as null:
            Popen(cmd, stdout=null, stderr=null).wait()
    except OSError:
        self.log.error(NO_LATEX_ERROR % self.latex_cmd)
    self.latex_run_counter += 1
    fname = '%s.log' % self.project_name
    with codecs.open(fname, 'r', 'utf-8', 'replace') as fobj:
        self.out = fobj.read()
    self.check_errors()