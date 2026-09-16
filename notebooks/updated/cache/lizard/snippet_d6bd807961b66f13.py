def frames(self, flush=True):
    self.flush()
    ret_val, frame = self._sensor.read()
    if not ret_val:
        raise Exception(
            'Unable to retrieve frame from OpenCVCameraSensor for id {0}'.
            format(self._device_id))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if self._upside_down:
        frame = np.flipud(frame).astype(np.uint8)
        frame = np.fliplr(frame).astype(np.uint8)
    return ColorImage(frame)