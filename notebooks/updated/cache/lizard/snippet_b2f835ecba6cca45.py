def remove_all(self):
    names = sorted(self._actions_dict.keys())
    for name in names:
        self.remove(name)