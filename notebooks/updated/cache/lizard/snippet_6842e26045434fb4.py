def _guessunit(self):
    if not self.days % 1:
        return 'd'
    elif not self.hours % 1:
        return 'h'
    elif not self.minutes % 1:
        return 'm'
    elif not self.seconds % 1:
        return 's'
    else:
        raise ValueError(
            'The stepsize is not a multiple of one second, which is not allowed.'
            )