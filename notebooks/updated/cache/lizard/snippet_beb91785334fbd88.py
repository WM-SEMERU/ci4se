def challenge_response(self, challenge, mode='HMAC', slot=1, variable=True,
    may_block=True):
    if not self.capabilities.have_challenge_response(mode):
        raise yubikey_base.YubiKeyVersionError(
            '%s challenge-response unsupported in YubiKey %s' % (mode, self
            .version()))
    return self._challenge_response(challenge, mode, slot, variable, may_block)