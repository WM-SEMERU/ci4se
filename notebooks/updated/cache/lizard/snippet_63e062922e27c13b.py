def _methodInTraceback(self, name, traceback):
    foundMethod = False
    for frame in self._frames(traceback):
        this = frame.f_locals.get('self')
        if this is self and frame.f_code.co_name == name:
            foundMethod = True
            break
    return foundMethod