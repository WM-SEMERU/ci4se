def build_error_handler(*tasks):

    def _handler(error, tasks=[]):
        [t(error) for t in tasks]
        return error.jsonify(), error.status_code, error.headers
    return functools.partial(_handler, tasks=tasks)