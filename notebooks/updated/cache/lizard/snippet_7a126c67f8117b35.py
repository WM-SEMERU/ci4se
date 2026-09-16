def run_to_abs_pos(self, **kwargs):
    for key in kwargs:
        setattr(self, key, kwargs[key])
    self.command = self.COMMAND_RUN_TO_ABS_POS