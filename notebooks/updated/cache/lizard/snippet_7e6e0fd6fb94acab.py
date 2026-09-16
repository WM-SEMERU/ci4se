def mesh(self):
    triangles = np.empty((self.f.shape[0], 4))
    triangles[:, -3:] = self.f
    triangles[:, (0)] = 3
    return vtki.PolyData(self.v, triangles, deep=False)