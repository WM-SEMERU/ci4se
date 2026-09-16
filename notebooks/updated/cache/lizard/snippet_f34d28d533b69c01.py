def coordinates(self, transformed=True, copy=True):
    poly = self.polydata(transformed)
    if copy:
        return np.array(vtk_to_numpy(poly.GetPoints().GetData()))
    else:
        return vtk_to_numpy(poly.GetPoints().GetData())