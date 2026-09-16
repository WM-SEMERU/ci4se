def _read_metadata(self):
    if self._is_metadata_init():
        return
    try:
        log.debug('Reading metadata of "{path}" ...'.format(path=self.
            _filepath))
        data = metadata.parse(self._filepath)
        videotracks = data.get_videotracks()
        if len(videotracks) > 0:
            self._fps = videotracks[0].get_framerate()
            self._time_ms = videotracks[0].get_duration_ms()
            self._framecount = videotracks[0].get_framecount()
    except:
        log.debug('... FAIL')
        log.exception('Exception was thrown.')