def get_point_group_symbol(self):
    rotations = self._space_group_data['rotations']
    if len(rotations) == 0:
        return '1'
    return spglib.get_pointgroup(rotations)[0].strip()