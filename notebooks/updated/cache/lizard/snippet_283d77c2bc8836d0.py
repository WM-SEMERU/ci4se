def _select_position(self, width, height):
    positions = self._generate_placements(width, height)
    if self.rot and width != height:
        positions += self._generate_placements(height, width)
    if not positions:
        return None, None
    return min(((p[0], self._rect_fitness(*p)) for p in positions), key=
        operator.itemgetter(1))