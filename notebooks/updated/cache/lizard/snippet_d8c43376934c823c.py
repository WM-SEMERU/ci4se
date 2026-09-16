def _arg_varname(self, wire):
    if isinstance(wire, (Input, Register)):
        return 'd[' + repr(wire.name) + ']'
    elif isinstance(wire, Const):
        return str(wire.val)
    else:
        return self._varname(wire)