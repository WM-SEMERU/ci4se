def share(self, data, mime=None, time=None):
    evt = self.share_async(data, mime=mime, time=time)
    self._client._wait_and_except_if_failed(evt)