def run(self):
    if self.on_start:
        self.on_start(self)
    try:
        result = self.func(*self.func_args, **self.func_kwargs)
    except Exception as err:
        self.to_failed()
        if self.on_error:
            self.on_error(self, err)
        raise
    self.to_success()
    if self.on_success:
        self.on_success(self, result)
    return result