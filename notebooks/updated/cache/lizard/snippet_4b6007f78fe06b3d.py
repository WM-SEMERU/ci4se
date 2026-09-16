def down(self, point):
    self._pdown = np.array(point, dtype=np.float32)
    self._pose = self._n_pose
    self._target = self._n_target