def _map_generator(f, generator):
    item = next(generator)
    while True:
        try:
            result = yield f(item)
        except Exception:
            item = generator.throw(*sys.exc_info())
        else:
            item = generator.send(result)