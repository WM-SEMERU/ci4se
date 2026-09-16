def print_info(self, obj=None, buf=sys.stdout):
    if not obj:
        self._print_info(buf)
        return True
    b = False
    for fn in (self._print_tool_info, self._print_package_info, self.
        _print_suite_info, self._print_context_info):
        b_ = fn(obj, buf, b)
        b |= b_
        if b_:
            print >> buf, ''
    if not b:
        print >> buf, "Rez does not know what '%s' is" % obj
    return b