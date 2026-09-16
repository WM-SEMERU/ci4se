def generate_private_key(key_size=2048):
    return cryptography.hazmat.primitives.asymmetric.rsa.generate_private_key(
        public_exponent=65537, key_size=key_size, backend=cryptography.
        hazmat.backends.default_backend())