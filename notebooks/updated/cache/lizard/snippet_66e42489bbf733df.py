def post_execute(self):
    result = super(Sink, self).post_execute()
    if result is None:
        self._input = None
    return result