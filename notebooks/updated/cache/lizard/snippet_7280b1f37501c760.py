def _add_tile(self, new_tile, ijk):
    tile_label = '{0}_{1}'.format(self.name, '-'.join(str(d) for d in ijk))
    self.add(new_tile, label=tile_label, inherit_periodicity=False)