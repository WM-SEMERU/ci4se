def get_multi(cls, blob_keys, **ctx_options):
    futs = cls.get_multi_async(blob_keys, **ctx_options)
    return [fut.get_result() for fut in futs]