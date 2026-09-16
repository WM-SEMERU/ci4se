def stream(self, item, *, device_id=None, quality='hi', session_token=None):
    if device_id is None:
        device_id = self.device_id
    stream_url = self.stream_url(item, device_id=device_id, quality=quality,
        session_token=session_token)
    response = self.session.get(stream_url)
    audio = response.content
    return audio