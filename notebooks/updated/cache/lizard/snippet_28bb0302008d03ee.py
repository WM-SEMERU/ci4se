def get_binary_iterator(self):
    CHUNK_SIZE = 1024
    file_object = open(self.path)
    while True:
        data = file_object.read(CHUNK_SIZE)
        if not data:
            break
        yield data
    file_object.close()