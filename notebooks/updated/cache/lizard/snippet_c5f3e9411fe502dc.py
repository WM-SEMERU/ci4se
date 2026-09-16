def decrypt(**kwargs):
    with StreamDecryptor(**kwargs) as decryptor:
        plaintext = decryptor.read()
    return plaintext, decryptor.header