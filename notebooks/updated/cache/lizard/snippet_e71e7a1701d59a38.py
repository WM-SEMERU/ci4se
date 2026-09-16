def merged_series(cls, *series, **kwargs):
    router, backend = cls.check_router(None, *series)
    if backend:
        target = router.register(cls(), backend)
        router.session().add(target)
        target._merge(*series, **kwargs)
        backend = target.backend
        return backend.execute(backend.structure(target).irange_and_delete(
            ), target.load_data)