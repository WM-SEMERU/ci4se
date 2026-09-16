def encrypt(**kwargs):
    with StreamEncryptor(**kwargs) as encryptor:
        ciphertext = encryptor.read()
    return ciphertext, encryptor.header