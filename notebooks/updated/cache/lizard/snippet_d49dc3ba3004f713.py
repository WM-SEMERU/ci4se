def readinto(self, byte_array):
    max_size = len(byte_array)
    data = self.read(max_size)
    bytes_read = len(data)
    byte_array[:bytes_read] = data
    return bytes_read