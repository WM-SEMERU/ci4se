def set_calibration(self, delta: Point):
    self._calibrated_offset = Point(x=self._offset.x + delta.x, y=self.
        _offset.y + delta.y, z=self._offset.z + delta.z)
    self._wells = self._build_wells()