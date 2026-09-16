def concat_stim(self, decon_stim):
    if self.type() != decon_stim.type():
        nl.notify(
            'Error: Trying to concatenate stimuli of different types! %s (%s) with %s (%s)'
             % (self.name, self.type(), decon_stim.name, decon_stim.type()),
            level=nl.level.error)
        return None
    concat_stim = copy.copy(self)
    if self.name == 'Blank':
        concat_stim = copy.copy(decon_stim)
    self.read_file()
    if self.type() == 'column':
        reps = [(x.reps if x.reps else len(x.column)) for x in [self,
            decon_stim]]
        concat_stim.column = self.column[:reps[0]] + decon_stim.column[:reps[1]
            ]
        return concat_stim
    if self.type() == 'times':
        if len(self.times) == 0 or '__iter__' not in dir(self.times[0]):
            self.times = [self.times]
        if len(decon_stim.times) == 0 or '__iter__' not in dir(decon_stim.
            times[0]):
            decon_stim.times = [decon_stim.times]
        concat_stim.times = self.times + decon_stim.times
        return concat_stim
    return None