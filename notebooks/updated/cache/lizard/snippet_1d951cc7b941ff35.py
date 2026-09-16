def has_face_color(self):
    for v in (self._face_colors, self._face_colors_indexed_by_faces, self.
        _face_colors_indexed_by_edges):
        if v is not None:
            return True
    return False