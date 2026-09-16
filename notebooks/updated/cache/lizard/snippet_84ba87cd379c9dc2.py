def points(self):
    x = vtk_to_numpy(self.GetXCoordinates())
    y = vtk_to_numpy(self.GetYCoordinates())
    z = vtk_to_numpy(self.GetZCoordinates())
    xx, yy, zz = np.meshgrid(x, y, z, indexing='ij')
    return np.c_[xx.ravel(), yy.ravel(), zz.ravel()]