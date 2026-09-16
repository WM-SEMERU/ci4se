def _set_arg_generic(self, argid, arg, cast=str):
    usable, filename, append = self._redirect_split(arg)
    if usable != '':
        self.curargs[argid] = cast(usable)
    if argid in self.curargs:
        result = "{}: '{}'".format(argid.upper(), self.curargs[argid])
        self._redirect_output(result, filename, append, msg.info)