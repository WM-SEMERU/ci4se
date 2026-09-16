def stats(self, container, decode=None, stream=True):
    url = self._url('/containers/{0}/stats', container)
    if stream:
        return self._stream_helper(self._get(url, stream=True), decode=decode)
    else:
        if decode:
            raise errors.InvalidArgument(
                'decode is only available in conjuction with stream=True')
        return self._result(self._get(url, params={'stream': False}), json=True
            )