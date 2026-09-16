def _check_backend():
    middleware = set(getattr(settings, 'MIDDLEWARE', None) or getattr(
        settings, 'MIDDLEWARE_CLASSES', None) or [])
    if 'djconfig.middleware.DjConfigLocMemMiddleware' in middleware:
        return
    if 'djconfig.middleware.DjConfigMiddleware' in middleware:
        return
    raise ValueError(
        'djconfig.middleware.DjConfigMiddleware is required but it was not found in MIDDLEWARE_CLASSES nor in MIDDLEWARE'
        )