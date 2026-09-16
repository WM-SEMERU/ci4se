def presence_handler(stream, type_, from_, cb):
    stream.register_presence_callback(type_, from_, cb)
    try:
        yield
    finally:
        stream.unregister_presence_callback(type_, from_)