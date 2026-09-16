def wrap(self, main_phases, name=None):
    new_main = list(self.main)
    if isinstance(main_phases, collections.Iterable):
        new_main.extend(main_phases)
    else:
        new_main.append(main_phases)
    return PhaseGroup(setup=self.setup, main=new_main, teardown=self.
        teardown, name=name)