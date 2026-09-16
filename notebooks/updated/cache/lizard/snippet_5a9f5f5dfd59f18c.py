def collect(cls, result_key, func):

    def scanner(self, obj):
        if not getattr(self, result_key, None):
            setattr(self, result_key, [])
        rv = func(obj)
        if rv:
            getattr(self, result_key).append(rv)
    cls._scan(result_key, scanner)