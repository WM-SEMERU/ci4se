def get_exception(self):
    if self.exc_info:
        try:
            six.reraise(*self.exc_info)
        except Exception as e:
            return e