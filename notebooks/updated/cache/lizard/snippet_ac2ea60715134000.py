def read_epub(name, options=None):
    reader = EpubReader(name, options)
    book = reader.load()
    reader.process()
    return book