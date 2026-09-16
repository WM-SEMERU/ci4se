def get_orientation_radians(self):
    raw = self._get_raw_data('fusionPoseValid', 'fusionPose')
    if raw is not None:
        raw['roll'] = raw.pop('x')
        raw['pitch'] = raw.pop('y')
        raw['yaw'] = raw.pop('z')
        self._last_orientation = raw
    return deepcopy(self._last_orientation)