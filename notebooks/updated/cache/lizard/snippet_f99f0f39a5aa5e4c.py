def load_all(stream, Loader=None):
    if Loader is None:
        load_warning('load_all')
        Loader = FullLoader
    loader = Loader(stream)
    try:
        while loader.check_data():
            yield loader.get_data()
    finally:
        loader.dispose()