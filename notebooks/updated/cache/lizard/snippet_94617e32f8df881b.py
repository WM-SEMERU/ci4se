def db_for_write(self, model, **hints):
    try:
        if model.sf_access == READ_ONLY:
            raise WriteNotSupportedError('%r is a read-only model.' % model)
    except AttributeError:
        pass
    return None