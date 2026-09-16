def send_env_text(self, text, episode_id):
    reactor.callFromThread(self._send_env_text, text, episode_id)