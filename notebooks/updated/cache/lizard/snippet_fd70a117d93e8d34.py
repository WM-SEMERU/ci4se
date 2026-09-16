def encrypt(plaintext_str, keys):
    assert keys, 'Must provide at least one key to encrypt with'
    ctx = gpg.core.Context(armor=True)
    out = ctx.encrypt(plaintext_str, recipients=keys, sign=False,
        always_trust=True)[0]
    return out