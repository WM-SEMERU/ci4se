def cut_sphere(self, radius=15.0, origin=None, outside_sliced=True,
    preserve_bonds=False):
    if origin is None:
        origin = np.zeros(3)
    elif pd.api.types.is_list_like(origin):
        origin = np.array(origin, dtype='f8')
    else:
        origin = self.loc[origin, ['x', 'y', 'z']]
    molecule = self.get_distance_to(origin)
    if outside_sliced:
        molecule = molecule[molecule['distance'] < radius]
    else:
        molecule = molecule[molecule['distance'] > radius]
    if preserve_bonds:
        molecule = self._preserve_bonds(molecule)
    return molecule