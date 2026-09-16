def Execute(self, action, *args, **kw):
    action = self.Action(action, *args, **kw)
    result = action([], [], self)
    if isinstance(result, SCons.Errors.BuildError):
        errstr = result.errstr
        if result.filename:
            errstr = result.filename + ': ' + errstr
        sys.stderr.write('scons: *** %s\n' % errstr)
        return result.status
    else:
        return result