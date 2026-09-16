def set_active_vectors(self, name, preference='cell'):
    _, field = get_scalar(self, name, preference=preference, info=True)
    if field == POINT_DATA_FIELD:
        self.GetPointData().SetActiveVectors(name)
    elif field == CELL_DATA_FIELD:
        self.GetCellData().SetActiveVectors(name)
    else:
        raise RuntimeError('Data field ({}) not useable'.format(field))
    self._active_vectors_info = [field, name]