def double_tap(self, on_element):
    self._actions.append(lambda : self._driver.execute(Command.DOUBLE_TAP,
        {'element': on_element.id}))
    return self