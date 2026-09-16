def print_detailed_traceback(self, space=None, file=None):
    if file is None:
        file = sys.stderr
    f = io.StringIO()
    for i in range(len(self.debug_excs) - 1, -1, -1):
        print >> f, 'Traceback (interpreter-level):'
        traceback.print_tb(self.debug_excs[i][2], file=f)
    f.seek(0)
    debug_print(''.join([('|| ' + line) for line in f.readlines()]), file)
    if self.debug_excs:
        from pypy.tool import tb_server
        tb_server.publish_exc(self.debug_excs[-1])
    self.print_app_tb_only(file)
    print >> file, '(application-level)', self.errorstr(space)
    if AUTO_DEBUG:
        debug.fire(self)