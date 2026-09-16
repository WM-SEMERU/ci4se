def do_cd(self, arglist):
    if not arglist or len(arglist) != 1:
        self.perror('cd requires exactly 1 argument:', traceback_war=False)
        self.do_help('cd')
        self._last_result = cmd2.CommandResult('', 'Bad arguments')
        return
    path = os.path.abspath(os.path.expanduser(arglist[0]))
    out = ''
    err = None
    data = None
    if not os.path.isdir(path):
        err = '{!r} is not a directory'.format(path)
    elif not os.access(path, os.R_OK):
        err = 'You do not have read access to {!r}'.format(path)
    else:
        try:
            os.chdir(path)
        except Exception as ex:
            err = '{}'.format(ex)
        else:
            out = 'Successfully changed directory to {!r}\n'.format(path)
            self.stdout.write(out)
            data = path
    if err:
        self.perror(err, traceback_war=False)
    self._last_result = cmd2.CommandResult(out, err, data)