def execute(self, data_dict, callback, group=None, trace=None):
    group = group or self.group
    context = _ScopedContext(data_dict, self.undefined_str, group=group)
    _Execute(self._program.Statements(), context, callback, trace)