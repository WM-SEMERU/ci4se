def instance(cls, size):
    if not getattr(cls, '_instance', None):
        cls._instance = {}
    if size not in cls._instance:
        cls._instance[size] = ThreadPool(size)
    return cls._instance[size]