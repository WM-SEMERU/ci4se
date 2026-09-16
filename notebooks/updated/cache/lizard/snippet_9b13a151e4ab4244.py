def add_update_callback(self, group=None, name=None, cb=None):
    if not group and not name:
        self.all_update_callback.add_callback(cb)
    elif not name:
        if group not in self.group_update_callbacks:
            self.group_update_callbacks[group] = Caller()
        self.group_update_callbacks[group].add_callback(cb)
    else:
        paramname = '{}.{}'.format(group, name)
        if paramname not in self.param_update_callbacks:
            self.param_update_callbacks[paramname] = Caller()
        self.param_update_callbacks[paramname].add_callback(cb)