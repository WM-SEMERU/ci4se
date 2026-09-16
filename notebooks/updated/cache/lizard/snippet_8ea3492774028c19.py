def _record_buffer(records, buffer_size=DEFAULT_BUFFER_SIZE):
    with tempfile.SpooledTemporaryFile(buffer_size, mode='wb+') as tf:
        pickler = pickle.Pickler(tf)
        for record in records:
            pickler.dump(record)

        def record_iter():
            tf.seek(0)
            unpickler = pickle.Unpickler(tf)
            while True:
                try:
                    yield unpickler.load()
                except EOFError:
                    break
        yield record_iter