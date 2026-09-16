def isCryptographyAdvanced():
    try:
        from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
        X25519PrivateKey.generate()
    except Exception:
        return False
    else:
        return True