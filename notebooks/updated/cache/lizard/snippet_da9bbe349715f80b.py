def decrypt(text, key=None):
    if key is None:
        key = ENCRYPT_KEY
    bits = len(key)
    text = base64.b64decode(text)
    iv = text[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(text[16:]))