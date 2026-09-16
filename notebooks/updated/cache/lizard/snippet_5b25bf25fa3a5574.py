def parse(cls, backend, ik, spk, spk_signature, otpks):
    ik = backend.decodePublicKey(ik)[0]
    spk['key'] = backend.decodePublicKey(spk['key'])[0]
    otpks = list(map(lambda otpk: {'key': backend.decodePublicKey(otpk[
        'key'])[0], 'id': otpk['id']}, otpks))
    return cls(ik, spk, spk_signature, otpks)