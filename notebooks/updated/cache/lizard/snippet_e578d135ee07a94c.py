def cartoon(self, cmap=None):
    top = self.topology
    geom = gg.GeomProteinCartoon(gg.Aes(xyz=self.coordinates, types=top[
        'atom_names'], secondary_type=top['secondary_structure']), cmap=cmap)
    primitives = geom.produce(gg.Aes())
    ids = [self.add_representation(r['rep_type'], r['options']) for r in
        primitives]

    def update(self=self, geom=geom, ids=ids):
        primitives = geom.produce(gg.Aes(xyz=self.coordinates))
        [self.update_representation(id_, rep_options) for id_, rep_options in
            zip(ids, primitives)]
    self.update_callbacks.append(update)
    self.autozoom(self.coordinates)