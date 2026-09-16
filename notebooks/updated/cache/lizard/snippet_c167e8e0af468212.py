def apply(self, callback, context):

    def wrapper(*args, **kwargs):
        try:
            return callback(*args, **kwargs)
        except bottle.HTTPError as error:
            return self.error_wrapper.from_status(status_line=error.
                status_line, msg=error.body)
    return wrapper