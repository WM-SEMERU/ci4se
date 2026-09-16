def from_raw_seed(cls, raw_seed):
    signing_key = ed25519.SigningKey(raw_seed)
    verifying_key = signing_key.get_verifying_key()
    return cls(verifying_key, signing_key)