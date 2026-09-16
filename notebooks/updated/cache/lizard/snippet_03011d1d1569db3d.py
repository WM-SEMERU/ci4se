def inverse(self):
    inv_rot = np.linalg.inv(self.rotation)
    inv_scale = 1.0 / self.scale
    inv_trans = -inv_scale * inv_rot.dot(self.translation)
    return SimilarityTransform(inv_rot, inv_trans, inv_scale, from_frame=
        self._to_frame, to_frame=self._from_frame)