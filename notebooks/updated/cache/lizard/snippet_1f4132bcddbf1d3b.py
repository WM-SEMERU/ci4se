def sealedbox_decrypt(data, **kwargs):
    if data is None:
        return None
    data = salt.utils.stringutils.to_bytes(data)
    sk = _get_sk(**kwargs)
    keypair = libnacl.public.SecretKey(sk)
    b = libnacl.sealed.SealedBox(keypair)
    return b.decrypt(base64.b64decode(data))