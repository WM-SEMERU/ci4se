def get_state(self, force_update=False):
    if force_update or self._state is None:
        return int(self.maker_attribs.get('switchstate', 0))
    return self._state