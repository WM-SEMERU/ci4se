def uri2module(self, uri):
    compressed = zlib.compress(uri)
    encoded = base64.b64encode(compressed, b'+&')
    encoded_str = encoded.decode('ASCII')
    return super(EncodedModuleLoader, self).uri2module(encoded_str)