def setReference(self, ref):
    self.quad = None
    self._camera_position = None
    self._homography = None
    self._homography_is_fixed = True
    self._pose = None
    if isinstance(ref, np.ndarray) and ref.shape == (3, 3):
        self._homography = ref
    elif len(ref) == 4:
        self.quad = sortCorners(ref)
        o = self.obj_points
    else:
        self.ref = imread(ref)
        self.pattern = PatternRecognition(self.ref)
        self._homography_is_fixed = False