def save(self, file):
    w = Writer(**self.info)
    try:
        file.write

        def close():
            pass
    except AttributeError:
        file = open(file, 'wb')

        def close():
            file.close()
    try:
        w.write(file, self.rows)
    finally:
        close()