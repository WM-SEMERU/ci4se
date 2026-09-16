def _wrapper(self):
    try:
        res = self.func(*self.args, **self.kw)
    except Exception as e:
        self.mediator.set_error(e)
    else:
        self.mediator.set_result(res)