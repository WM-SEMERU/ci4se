def rotate_capture_handler_log(self, name):
    for sc_key, sc in self._stream_capturers.iteritems():
        for h in sc[0].capture_handlers:
            if h['name'] == name:
                sc[0]._rotate_log(h)