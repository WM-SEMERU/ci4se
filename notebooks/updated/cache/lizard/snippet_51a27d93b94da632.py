def remove_step_method(self, step_method):
    try:
        for s in step_method.stochastics:
            self.step_method_dict[s].remove(step_method)
        if hasattr(self, 'step_methods'):
            self.step_methods.discard(step_method)
        self._sm_assigned = False
    except AttributeError:
        for sm in step_method:
            self.remove_step_method(sm)