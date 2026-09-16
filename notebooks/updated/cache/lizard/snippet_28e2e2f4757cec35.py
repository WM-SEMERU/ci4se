def update_columns(self, field, value_dict, inds=None, computed_type=None):
    if not isinstance(value_dict, dict):
        value_dict = {comp_no: value_dict for comp_no in self._dict.keys()}
    for comp, value in value_dict.items():
        if computed_type is not None:
            self._dict[comp]._observables[field] = ComputedColumn(self.
                _dict[comp], compute_at_vertices=computed_type == 'vertices')
        if inds:
            raise NotImplementedError(
                'setting column with indices not yet ported to new meshing')
        elif comp in self._dict.keys():
            self._dict[comp][field] = value
        else:
            meshes = self._dict[self._parent_envelope_of[comp]]
            meshes[comp][field] = value