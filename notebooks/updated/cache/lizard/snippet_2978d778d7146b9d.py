def connect(self, *args, **kwargs):
    if hasattr(self, '_vcr_request') and self.cassette.can_play_response_for(
        self._vcr_request):
        return
    if self.cassette.write_protected:
        return
    from vcr.patch import force_reset
    with force_reset():
        return self.real_connection.connect(*args, **kwargs)
    self._sock = VCRFakeSocket()