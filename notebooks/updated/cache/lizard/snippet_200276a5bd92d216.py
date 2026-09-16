def blank_stim(self, type=None, fill=0):
    blank = copy.copy(self)
    blank.name = 'Blank'
    if type == None:
        type = self.type()
    if type == 'column':
        num_reps = self.reps
        if num_reps == None:
            if self.type() == 'column':
                self.read_file()
                num_reps = len(self.column)
            else:
                nl.notify(
                    "Error: requested to return a blank column, but I can't figure out how many reps to make it!"
                    , level=nl.level.error)
        blank.column = [fill] * num_reps
        return blank
    if type == 'times':
        blank.times = []
        return blank