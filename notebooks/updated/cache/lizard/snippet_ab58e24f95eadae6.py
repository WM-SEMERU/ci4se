def make_ready_current(self):
    global print_prepare
    T = self.tm.trace
    if T:
        T.write(self.trace_message('Task.make_ready_current()', self.node))
    self.out_of_date = []
    needs_executing = False
    for t in self.targets:
        try:
            t.disambiguate().make_ready()
            is_up_to_date = not t.has_builder(
                ) or not t.always_build and t.is_up_to_date()
        except EnvironmentError as e:
            raise SCons.Errors.BuildError(node=t, errstr=e.strerror,
                filename=e.filename)
        if not is_up_to_date:
            self.out_of_date.append(t)
            needs_executing = True
    if needs_executing:
        for t in self.targets:
            t.set_state(NODE_EXECUTING)
            for s in t.side_effects:
                s.disambiguate().set_state(NODE_EXECUTING)
    else:
        for t in self.targets:
            t.visited()
            t.set_state(NODE_UP_TO_DATE)
            if not print_prepare and (not hasattr(self, 'options') or not
                self.options.debug_includes):
                t.release_target_info()