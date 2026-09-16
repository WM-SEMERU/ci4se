def make_filename_hash(key):
    key_repr = repr(key).replace(BASE_DIR, '').encode('utf8')
    if sys.platform == 'win32':
        key_repr = key_repr.replace(b'\\\\', b'/')
    key_repr = re.sub(b"\\bu'", b"'", key_repr)
    key_hash = hashlib.md5(key_repr).digest()
    return base64.b64encode(key_hash, b'__').decode('ascii').rstrip('=')