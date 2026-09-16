def prepare(session_data={}, passphrase=None):
    if passphrase is None:
        passphrase = settings.DJAODJIN_SECRET_KEY
    return encode(session_data, passphrase, json_encoder=crypt.JSONEncoder)