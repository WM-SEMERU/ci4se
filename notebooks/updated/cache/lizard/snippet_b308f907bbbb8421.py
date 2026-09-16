def location(self):
    if self._w3c:
        old_loc = self._execute(Command.GET_ELEMENT_RECT)['value']
    else:
        old_loc = self._execute(Command.GET_ELEMENT_LOCATION)['value']
    new_loc = {'x': round(old_loc['x']), 'y': round(old_loc['y'])}
    return new_loc