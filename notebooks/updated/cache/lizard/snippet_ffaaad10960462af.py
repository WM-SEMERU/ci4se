def binary(self, length=1 * 1024 * 1024):
    blob = [self.generator.random.randrange(256) for _ in range(length)]
    return bytes(blob) if sys.version_info[0] >= 3 else bytearray(blob)