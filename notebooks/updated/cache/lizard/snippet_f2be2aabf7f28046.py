def cache_file(package, mode):
    f = DummyFile()
    with exception_to_warning('use cache while checking for outdated package',
        OutdatedCacheFailedWarning):
        try:
            cache_path = os.path.join(tempfile.gettempdir(),
                get_cache_filename(package))
            if mode == 'w' or os.path.exists(cache_path):
                f = open(cache_path, mode)
        finally:
            with f:
                yield f