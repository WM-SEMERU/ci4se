def get_optimization_coordinates(self):
    coor_array = self.fields.get('Opt point       1 Geometries')
    if coor_array is None:
        return []
    else:
        return np.reshape(coor_array, (-1, len(self.molecule.numbers), 3))