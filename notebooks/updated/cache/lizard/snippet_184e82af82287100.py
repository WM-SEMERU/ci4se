def send_message(self, stream, msg):
    assert get_thread_ident() == self.ioloop_thread_id
    try:
        if stream.KATCPServer_closing:
            raise RuntimeError(
                'Stream is closing so we cannot accept any more writes')
        return stream.write(str(msg) + '\n')
    except Exception:
        addr = self.get_address(stream)
        self._logger.warn('Could not send message {0!r} to {1}'.format(str(
            msg), addr), exc_info=True)
        stream.close(exc_info=True)