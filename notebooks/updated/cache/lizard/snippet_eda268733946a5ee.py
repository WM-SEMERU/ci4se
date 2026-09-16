def _verifyHostKey(self, hostKey, fingerprint):
    if fingerprint in self.knownHosts:
        return defer.succeed(True)
    return defer.fail(UnknownHostKey(hostKey, fingerprint))