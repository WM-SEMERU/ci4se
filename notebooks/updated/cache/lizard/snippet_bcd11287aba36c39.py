def patch_all():
    global _patched
    if _patched:
        return
    _patched = True
    patch_default_retcodes()
    patch_worker_run_task()
    patch_worker_factory()
    patch_keepalive_run()
    patch_cmdline_parser()
    logger.debug('applied law-specific luigi patches')