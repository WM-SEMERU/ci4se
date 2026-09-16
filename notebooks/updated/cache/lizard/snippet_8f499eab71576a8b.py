def start_recording(self, output_file):
    if not self._started:
        raise Exception(
            'Must start the video recorder first by calling .start()!')
    if self._recording:
        raise Exception('Cannot record a video while one is already recording!'
            )
    self._recording = True
    self._cmd_q.put(('start', output_file))