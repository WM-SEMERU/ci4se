def close(self):
    cache_key = self._cache_key()
    SSH_CONNECTION_CACHE.pop(cache_key, None)
    SFTP_CONNECTION_CACHE.pop(cache_key, None)
    if self.sftp is not None:
        self.sftp.close()
    self.ssh.close()