def module2uri(self, module_name):
    encoded_str = super(EncodedModuleLoader, self).module2uri(module_name)
    encoded = encoded_str.encode('ASCII')
    compressed = base64.b64decode(encoded, b'+&')
    return zlib.decompress(compressed)