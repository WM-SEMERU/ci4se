def stream(self, sha):
    hexsha, typename, size, stream = self._git.stream_object_data(bin_to_hex
        (sha))
    return OStream(hex_to_bin(hexsha), typename, size, stream)