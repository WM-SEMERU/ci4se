def get_control_mode(self, ids):
    to_get_ids = [id for id in ids if id not in self._known_mode]
    limits = self.get_angle_limit(to_get_ids, convert=False)
    modes = [('wheel' if limit == (0, 0) else 'joint') for limit in limits]
    self._known_mode.update(zip(to_get_ids, modes))
    return tuple(self._known_mode[id] for id in ids)