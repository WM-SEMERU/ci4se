def get_backend(backend):
    if backend == 'random':
        backends = list_backends()
        random.shuffle(backends)
        return backends[0]
    return backend