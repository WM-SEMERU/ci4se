def insert(cls, index, interceptor):
    cls._check(interceptor)
    cls._interceptors.insert(index, interceptor)