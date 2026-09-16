def get_starting_chunk(filename, length=1024):
    try:
        with open(filename, 'rb') as f:
            chunk = f.read(length)
            return chunk
    except IOError as e:
        print(e)