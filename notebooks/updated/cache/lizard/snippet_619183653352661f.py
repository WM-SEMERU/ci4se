def do_vim(self, arg):
    self.vimpdb = make_instance()
    self.vimpdb.set_trace_without_step(self.botframe)
    if self.has_gone_up():
        self.vimpdb.update_state(self)
        self.vimpdb.cmdloop()
    else:
        self.vimpdb.interaction(self.curframe, None)
    return 1