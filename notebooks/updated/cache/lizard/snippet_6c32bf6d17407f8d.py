def handle_error(self, error, req, schema, error_status_code=None,
    error_headers=None):
    logger.error(error)
    raise error