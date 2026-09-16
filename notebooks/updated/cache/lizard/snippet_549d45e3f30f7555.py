def facets_normal(self):
    if len(self.facets) == 0:
        return np.array([])
    area_faces = self.area_faces
    index = np.array([i[area_faces[i].argmax()] for i in self.facets])
    normals = self.face_normals[index]
    origins = self.vertices[self.faces[:, (0)][index]]
    self._cache['facets_origin'] = origins
    return normals